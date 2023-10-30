# main.py
from config import *
from sql_content import establish_database_connection, execute_sql_query
from email_content import generate_email_content, send_email
from excel_content import create_excel_file
from datetime import datetime, timedelta

current_date = datetime.now().strftime('%d/%m/%Y')
yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y')

def main():
    conn, cursor = establish_database_connection()

    if conn and cursor:
        # SQL queries
        query1 = f"SELECT form_name, form_id, COUNT(ems_push) AS ems_push, " \
                f"COUNT(dms_push) AS dms_push, COUNT(crm_push) AS crm_push, " \
                f"COUNT(id) - COUNT(crm_push) AS invalid,COUNT(id) AS Toatl FROM tb_tvs_zapier_dms_api_leads " \
                f"WHERE CONVERT(date, create_date) BETWEEN CONVERT(date, '{current_date}', 103) " \
                f"AND CONVERT(date, '{current_date}', 103) GROUP BY form_name, form_id"

        query2 = f"SELECT form_name, form_id, COUNT(ems_push) AS ems_push, " \
                f"COUNT(dms_push) AS dms_push, COUNT(crm_push) AS crm_push, " \
                f"COUNT(id) - COUNT(crm_push) AS invalid , COUNT(id) AS Toatl FROM tb_tvs_zapier_dms_api_leads " \
                f"WHERE CONVERT(date, create_date) BETWEEN CONVERT(date, '{yesterday_date}', 103) " \
                f"AND CONVERT(date, '{yesterday_date}', 103) GROUP BY form_name, form_id"

        rows_query1 = execute_sql_query(cursor, query1)
        rows_query2 = execute_sql_query(cursor, query2)

        excel_file_name = create_excel_file(rows_query1, rows_query2)

        from_email, from_password, to_email, cc_email, subject, body = generate_email_content()
        send_email(from_email, from_password, to_email, cc_email, subject, body, excel_file_name)

        # Close cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
