import psycopg2
from  config import host,user,password,db_name




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
    cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")


    #create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE PhoneBook(
    #             id serial PRIMARY KEY,
    #             name varchar(50) NOT NULL,
    #             surname varchar(50) NOT NULL,
    #             number varchar(50) NOT NULL)
    #             ;"""
    #     )   
    
    #     print("[INFO] Table created succecfully ")

    #insert data into a table
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """INSERT INTO PhoneBook (name,surname,number) VALUES
        #         ('Oleg','Stepanov','87024567890'),
        #         ('Miras','Esimov','87023333333'),
        #         ('Nurdaulet','Tolepov','87777777777'); """
        #     )

        #     print("[INFO] Data was succesfully inserted")

    # querying data from the tables (with different filters)
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT number FROM phonebook WHERE name = 'Oleg';
    #            SELECT name FROM phonebook WHERE number  = "87023333333""""
    #     )

    #     print(cursor.fetchone())

    #delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         DROP TABLE phonebook;"""
    #     )

    #     print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostreSQL connection closed")
