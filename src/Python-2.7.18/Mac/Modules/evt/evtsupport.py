# This script generates a Python interface for an Apple Macintosh Manager.
# It uses the "bgen" package to generate C code.
# The function specifications are generated by scanning the mamager's header file,
# using the "scantools" package (customized for this particular manager).

import string

# Declarations that change for each manager
MACHEADERFILE = 'Events.h'              # The Apple header file
MODNAME = '_Evt'                                # The name of the module
OBJECTNAME = 'Event'                    # The basic name of the objects used here
KIND = 'Record'                         # Usually 'Ptr' or 'Handle'

# The following is *usually* unchanged but may still require tuning
MODPREFIX = 'Evt'                       # The prefix for module-wide routines
OBJECTTYPE = OBJECTNAME + KIND          # The C type used to represent them
OBJECTPREFIX = MODPREFIX + 'Obj'        # The prefix for object methods
INPUTFILE = string.lower(MODPREFIX) + 'gen.py' # The file generated by the scanner
OUTPUTFILE = MODNAME + "module.c"       # The file generated by this program

from macsupport import *

# Create the type objects

#WindowPeek = OpaqueByValueType("WindowPeek", OBJECTPREFIX)

RgnHandle = FakeType("(RgnHandle)0")
# XXXX Should be next, but this will break a lot of code...
# RgnHandle = OpaqueByValueType("RgnHandle", "OptResObj")

KeyMap = ArrayOutputBufferType("KeyMap")
##MacOSEventKind = Type("MacOSEventKind", "h") # Old-style
##MacOSEventMask = Type("MacOSEventMask", "h") # Old-style
EventMask = Type("EventMask", "H")
EventKind = Type("EventKind", "H")

includestuff = includestuff + """
#include <Carbon/Carbon.h>

"""

# From here on it's basically all boiler plate...

# Create the generator groups and link them
module = MacModule(MODNAME, MODPREFIX, includestuff, finalstuff, initstuff)

# Create the generator classes used to populate the lists
Function = OSErrWeakLinkFunctionGenerator
##Method = OSErrWeakLinkMethodGenerator

# Create and populate the lists
functions = []
execfile(INPUTFILE)

# Move TickCount here, for convenience
f = Function(UInt32, 'TickCount',
)
functions.append(f)

# add the populated lists to the generator groups
# (in a different wordl the scan program would generate this)
for f in functions: module.add(f)

WaitNextEvent_body = """
Boolean _rv;
EventMask eventMask;
EventRecord theEvent;
UInt32 sleep;
Handle mouseregion = (Handle)0;

if (!PyArg_ParseTuple(_args, "Hl|O&",
                      &eventMask,
                      &sleep,
                      OptResObj_Convert, &mouseregion))
        return NULL;
_rv = WaitNextEvent(eventMask,
                    &theEvent,
                    sleep,
                    (RgnHandle)mouseregion);
_res = Py_BuildValue("bO&",
                     _rv,
                     PyMac_BuildEventRecord, &theEvent);
return _res;
"""
f = ManualGenerator("WaitNextEvent", WaitNextEvent_body);
f.docstring = lambda: "(EventMask eventMask, UInt32 sleep [,RegionHandle]) -> (Boolean _rv, EventRecord theEvent)"
module.add(f)


# generate output (open the output file as late as possible)
SetOutputFileName(OUTPUTFILE)
module.generate()
