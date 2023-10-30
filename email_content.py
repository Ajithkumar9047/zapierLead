# email_content.py
from config import *
current_date = datetime.now().strftime('%d/%m/%Y')
yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y')
def generate_email_content():
    from_email = 'ajithkumar@newgendigital.com'
    from_password = 'uroqpjoiixmnrxxb'
    to_email = 'lalit.vijay@adglobal360.com'
    cc_email = ' rahul.bansal@adglobal360.com , raghvendra.singh@adglobal360.com , harsh.sachdeva@adglobal360.com , arun.reddy@tvsmotor.com , prasanth.s@tvsmotor.com  '
    subject = '<Re: Zapier lead count>'
    body = f'''\
        <html>
        <head>
        <style>
            body {{
                font-family: Verdana, sans-serif;
                font-size: 14px;
                color: black;
            }}
            p {{
                margin: 10px 0;
            }}
        </style>
        </head>
        <body>
        <p>Hi all,</p>

        <p>Refer to the attachment below for details regarding the Zapier lead  count  form wise for the date {current_date}.</p>
        <p>Please confirm the count from your  end.</p>

        <b style="color: blue;">Thanks & Regards,<br></b>
        <p>Ajithkumar Sekar | Technical support executive<br>
        Newgen Digital Works Pvt. Ltd.<br>
        M: (+91) 8072467327<br>
        W: <a href="http://www.newgen.co">www.newgen.co</a><br>
        A: Chennai - 600041.</p>
        </body>
        </html>
        '''  # noqa: E501

    return from_email, from_password, to_email, cc_email, subject, body
def send_email(from_email, from_password, to_email, cc_email, subject, body, excel_file_name):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Cc'] = cc_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)

        recipients = [to_email] + cc_email.split(', ')
        
        # Determine the file extension of excel_file_name
        base_name, file_extension = os.path.splitext(excel_file_name)
        
        # Construct the new name for the Excel attachment with the original extension
        new_excel_file_name = f"{current_date.replace('/', '_')}-zapierleadcount{file_extension}"

        msg.attach(MIMEApplication(open(excel_file_name, 'rb').read(), Name=new_excel_file_name))
        excel_attachment = open(excel_file_name, 'rb')
        excel_part = MIMEApplication(excel_attachment.read(), Name=new_excel_file_name)
        excel_attachment.close()
        excel_part['Content-Disposition'] = f'attachment; filename="{new_excel_file_name}"'
        msg.attach(excel_part)
        
        server.sendmail(from_email, recipients, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        server.quit()
