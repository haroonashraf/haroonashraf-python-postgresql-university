#!/usr/bin/python
# import PostgreSQL adaptor to be used in Python (https://pypi.org/project/psycopg2/)
import psycopg2
# import config from postgresql-config.py
from postgresql_config import postgresql_config

def postgresql_universitydb_connect():
    """ PostgreSQL server Connection """
    conn = None
    # put configuration into params 
    params = postgresql_config()
    # connecting to the PostgreSQL server
    print('Establishing connecting with PostgreSQL database...')
    conn = psycopg2.connect(**params)
		
    # create a cursor
    cur = conn.cursor()
        
	# execute SELECT version statement
    print('The version (PostgreSQL):')
    cur.execute('SELECT version()')

    # show PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
       
	# close cursor
    cur.close()
    conn.close()
    print('Database connection has been closed.')

# call the connect() function
if __name__ == '__main__':
    postgresql_universitydb_connect()