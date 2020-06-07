# Python_2718_glibc2.15
Python 2.7.18 build using glibc 2.15 on ubuntu with enable_load_extension

#export LD_LIBRARY_PATH=newglibc:$LD_LIBRARY_PATH
```Python
import sys
import sqlite3
e=sys.exit
con = sqlite3.connect(":memory:")
con.enable_load_extension(True)
con.load_extension("/home/ubuntu/sqlite-parquet-vtable/build/linux/libparquet") 


#export LD_LIBRARY_PATH=/home/ubuntu/sqlite/lib

#tar -czvf 

from pysqlite2 import dbapi2 as sqlite3
con = sqlite3.connect(":memory:")
con.enable_load_extension(True)
con.load_extension("/home/ubuntu/query-partuet-files-using-sqlite-python/build/linux/libparquet") 



 os.environ.update(dict(LD_LIBRARY_PATH='/var/task/lib'))
#export LD_LIBRARY_PATH=newglibc:$LD_LIBRARY_PATH
objdump -p myprog
import platform,sqlite3
print("Oper Sys : %s %s" % (platform.system(), platform.release()))
print("Platform : %s %s" % (platform.python_implementation(),platform.python_version()))
print("SQLite   : %s" % (sqlite3.sqlite_version))


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception  as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception  as e:
        print(e)

def main():
    database = r"pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

def ptest():
    database = r"pythonsqlite.db"

    # create a database connection
    #conn = create_connection(database)

    # create tables
    if con is not None:
        print('connected')
        q="""CREATE VIRTUAL TABLE demo USING parquet('/home/ubuntu/sqlite-parquet-vtable/parquet-generator/99-rows-1.parquet')"""
        create_table(con, q)
        
        q="""SELECT * FROM demo"""
        cur = con.cursor()
        cur.execute(q)

        rows = cur.fetchall()
        for row in rows:
            print(row)
    else:
        print("Error! cannot create the database connection.")
if __name__ == '__main__':
    ptest()
    #main()

"""
>>> import sqlite3
>>> con = sqlite3.connect(":memory:")
>>> con.enable_load_extension(True)
>>> con.load_extension("./json1.so")
"""
```

