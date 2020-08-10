import psycopg2

def update(NationalCode, CustomerName):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="password69aliN",
            host="localhost",
            port="5432",
            database="TestDB"
        )

        cursor = connection.cursor()

        print(" Customer Table Before updating ")
        pg_select = """SELECT * FROM public."Customer" WHERE "NationalCode" = %s """
        cursor.execute(pg_select, (NationalCode, ))
        book_record = cursor.fetchall()
        print(book_record)

        # Update single record now

        pg_update = """update public. "Customer" set "CustomerName"=%s WHERE "NationalCode"=%s """
        cursor.execute(pg_update, (CustomerName,NationalCode))
        connection.commit()
        count = cursor.rowcount
        print(count, "successfully updating")




        print("Customer Table After updating record ")
        pg_select = """select * from public. "Customer" where "NationalCode"= %s"""
        cursor.execute(pg_select, (NationalCode,))
        Customer_record = cursor.fetchone()
        print(Customer_record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)
        connection = None

    finally:
        # closing database connection.
        if connection != None:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

