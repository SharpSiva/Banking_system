import os
import smtplib
import random
from email.message import EmailMessage

#Class Mail_send is used to Send OTP through Email

class Mail_send():
    #Calls at the time of Login,fetch user corresponding Email data from SQL.
    @staticmethod
    def mail_login(Acct_Number):
        import pyodbc
        db = pyodbc.connect('Driver=SQL Server;'
                            'server=localhost;'
                            'Database=Bank;'
                            'Trusted_connection=yes;')
        cursor_db = db.cursor()
        OTP = random.randint(1000, 9999)
        cursor_db.execute("Select Email_ID from tbl_Contact_info where Account_Number='"+Acct_Number+"'")
        tup=cursor_db.fetchone()
        YourMailID=''.join(tup)
        content = "Your OneTimePassword is {}".format(OTP)
        Email_Address=os.environ.get('Email_Address')
        Email_Password=os.environ.get('Email_Password')
        msg=EmailMessage()
        msg['Subject']='OTP'
        msg['From']=Email_Address
        msg['To']=YourMailID
        msg.set_content(content)
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(Email_Address,Email_Password)
                server.send_message(msg)
        except Exception:
            print("Something went wrong! Please check your Mail_id")
            return False
        else:
            print("Mail send successfully to Your Email_ID for Authentication!")
            #For Validating the OTP
            while True:
                Enter_OTP = input("Please Enter OTP:")
                if Enter_OTP == str(OTP):
                    print("Login Succesful")
                    # Enter_OTP=False
                    break
                elif Enter_OTP == 'Cancel':
                    exit()
                print("Please Enter Valid OTP")

    #Calls at time of Account creation.OTP send to Registered Email_ID for Authentication
    @staticmethod
    def mail_send_create(MailID):
        OTP = random.randint(1000, 9999)
        YourMailID =MailID
        content = "Your OneTimePassword is {}".format(OTP)
        Email_Address = os.environ.get('Email_Address')
        Email_Password = os.environ.get('Email_Password')
        msg = EmailMessage()
        msg['Subject'] = 'OTP'
        msg['From'] = Email_Address
        msg['To'] = YourMailID
        msg.set_content(content)
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(Email_Address, Email_Password)
                server.send_message(msg)
        except Exception:
            print("Something went wrong! Please check your Mail_id")
            return False
        else:
            print("Mail send successfully to Your Email")
            #For Validating the OTP
            while True:
                print("Enter Cancel to Exit")
                Enter_OTP = input("Please Enter OTP:")
                if Enter_OTP == str(OTP):
                    print("Login Succesful")
                    # Enter_OTP=False
                    break
                elif Enter_OTP == 'Cancel':
                    exit()
                print("Please Enter Valid OTP")

login=Mail_send()

