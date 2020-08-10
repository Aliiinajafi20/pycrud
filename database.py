import psycopg2


def connect():
    psycopg2.connect(user='postgres',password='password69aliN',database='TestDB',host='localhost')