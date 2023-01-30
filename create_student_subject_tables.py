#!/usr/bin/python

import psycopg2 
from postgresql_config import postgresql_config


def create_student_subject_tables():
    """ creating student and subject tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE student (
            student_id SERIAL PRIMARY KEY,
            student_name VARCHAR(55) NOT NULL
        )
        """,
        """ CREATE TABLE subject (
                subject_id SERIAL PRIMARY KEY,
                subject_name VARCHAR(255) NOT NULL
                )
              
        """)
    # set conn to None    
    conn = None
    # set params object to read the connection parameters from config function 
    params = postgresql_config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    # create both tables student and subject using for loop
    for command in commands:
        cur.execute(command)
    # close cursor
    cur.close()
    # save the changes
    conn.commit()
    # close the connection 
    conn.close()

# run create_tables() function
if __name__ == '__main__':
    create_student_subject_tables()