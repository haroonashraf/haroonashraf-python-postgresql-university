#!/usr/bin/python

import psycopg2
from postgresql_config import postgresql_config


def insert_four_subjects(subject_name):
    """ insert a new subject into the subject table """
    sql = """INSERT INTO subject(subject_name)
             VALUES(%s) RETURNING subject_id;"""
    conn = None
    subject_id = None
    
    # read university database configuration
    params = postgresql_config()
    # connect to the PostgreSQL database (university sample db)
    conn = psycopg2.connect(**params)
    # create a new cursor
    cur = conn.cursor()
    # execute the INSERT statement to add new subject
    cur.execute(sql, (subject_name,))
    # get the id
    subject_id = cur.fetchone()[0]
    # save the changes to the database
    conn.commit()
    # close the cursor and connection
    cur.close()
    conn.close()

if __name__ == '__main__':
    # insert four subjects into the subject table
    insert_four_subjects("Data Structure")
    insert_four_subjects("Aritficial Intelligence")
    insert_four_subjects("Data Analysis")
    insert_four_subjects("Business Intelligence")
    