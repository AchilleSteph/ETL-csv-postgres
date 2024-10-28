import psycopg2

#function run_query() to connect to postgressql database and run query  

def connecter_db():

    # connect db named WATER2
    conn = psycopg2.connect(
        host = "localhost",
        database = "WATER2",
        user = "postgres",
        password = "1234")
    return conn



