import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
sql1 = """
    INSERT INTO public."Test"("Vendor")
	VALUES (aaaa);
"""

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=os.getenv("host"),
            database=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Database connection closed.')

def disconnect():
    try:
        conn = psycopg2.connect(
            host=os.getenv("host"),
            database=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )
        cur = conn.cursor()
        cur.close()
        print('Database Closed')
    except:
        print('Not Connected to any databse')

def insertSql(sql,param):
    try:
        print(param)
        conn = psycopg2.connect(
        host=os.getenv("host"),
        database=os.getenv("database"),
        user=os.getenv("user"),
        password=os.getenv("password")
        )
        cur = conn.cursor()
        # get the generated id back
        # execute the INSERT statement
        cur.execute(sql,(param,))
        # get the generated id back
        # commit the changes to the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


        
if __name__ == '__main__':
    connect()
    insertSql(sql1,'CDW')
    disconnect()