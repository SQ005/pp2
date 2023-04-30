import psycopg2
from config import host,user,password,db_name



try:
    #connect to exist datebase
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )

    connection.autocommit = True
    #the cursoor for perfoming datebase operations 
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")


    #create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             nick_name varchar(50) NOT NULL);"""
    #     )   

    #     # connection commit()
    
    #     print("[INFO] Table created succecfully ")

    #insert data into a table
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name,nick_name) VALUES
            ('Oleg','87024567890'),
            ('Kuandyk','87023333333'),
            ('Nurdaulet','87777777777'); """
        )

        print("[INFO] Data was succesfully inserted")

    #get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
    #     )

    #     print(cursor.fetchone())

    #delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )

    #     print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostreSQL connection closed")