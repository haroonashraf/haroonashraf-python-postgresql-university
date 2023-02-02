# Introduction 
This is an introduction to Python PostgreSQL database.

# Getting Started
These files help us to connect to PosgreSQL database university created using psql shell locally.
The following prerequisites need to be met:
1.	PostgreSQL is installed locally 
2.	Univesity sample database is created in PostgreSQL using psql command prompt


# Build and Test
The files must run in the following order:
1. postgresql_university_database.ini must be created and stored in the same folder where these files are however this file is not included in the repo as it contains sensitive information to connect to university database
2. postgresql_config.py
3. postgresql_universitydb_connect.py
4. create_student_subject_tables.py
5. insert_four_subjects.py
6. update_datastructure_subject.py

# The ini file pattern
The excluded postgresql_university_database.ini file must be created using the following pattern:<br>
[postgresql] <br>
host=localhost <br>
database=university <br>
user=postgres <br>
password=<your chosen password>
