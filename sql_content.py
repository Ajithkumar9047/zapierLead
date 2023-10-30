from config import *

def establish_database_connection():
    server = '10.121.2.43'
    database = 'TVSM_BRAND_WEBSITE'
    username = 'ePageMaker'
    password = 'RTRabs180'
    driver = '{ODBC Driver 17 for SQL Server}'
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print("Failed to establish a database connection:", str(e))
        return None, None

def execute_sql_query(cursor, query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print("An error occurred while executing the SQL query:", str(e))
        return []