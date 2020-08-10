import psycopg2

def delete(NationalCode):
    try:
        connection = psycopg2.connect(user="postgres",
            password="password69aliN",
            host="localhost",
            port="5432",
            database="TestDB")

        cursor = connection.cursor()

        # Update single record now
        pg_delete = """Delete from public."Customer" where "NationalCode" = %s"""
        cursor.execute(pg_delete, (NationalCode, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully",count, "rows.")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)
        connection = None

    finally:
        # closing database connection.
        if connection != None:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


