#!/usr/bin/python

import psycopg2
from postgresql_config import postgresql_config



def update_datastructure_subject(subject_id, subject_name):
    """ update subject name based on the subject id """
    sql = """ UPDATE subject
                SET subject_name = %s
                WHERE subject_id = %s"""
    conn = None
    UpdateRows = 0
    
    # setup params as config object 
    params = postgresql_config()
    # connect to the PostgreSQL database
    conn = psycopg2.connect(**params)
    # create a new cursor
    cur = conn.cursor()
    # execute the UPDATE  statement to update subject name for subject id 1
    cur.execute(sql, (subject_name, subject_id))
    # store the updated row count into UpdateRows 
    UpdateRows = cur.rowcount
    # save the changes 
    conn.commit()
    # Close cursor and close connection
    cur.close()
    conn.close()

    return UpdateRows

#call function update_subject
if __name__ == '__main__':
    # Update subject id 1 with new name
    update_datastructure_subject(1, "Data Structures")