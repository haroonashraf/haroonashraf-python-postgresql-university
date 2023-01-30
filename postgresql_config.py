#!/usr/bin/python
# import configparser 
from configparser import ConfigParser
# define config function that calls postgresql_university_database.ini file to fetch PostgreSQL server details and credentials
def postgresql_config(filename='postgresql_university_database.ini', section='postgresql'):
    # setup a parser object 
    parser = ConfigParser()
    # call parser read method to read postgresql_university_database.ini
    parser.read(filename)

    # get the required db (university in our case)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    
    # return db    
    return db