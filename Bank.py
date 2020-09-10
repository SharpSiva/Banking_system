import random
import Email_Script_for_OTP
class Bank:
    def __init__(self):
        import pyodbc
        self.db = pyodbc.connect('Driver=SQL Server;'
                                 'server=localhost;'
                                 'Database=Bank;'
                                 'Trusted_connection=yes;')
        self.cursor = self.db.cursor()

    def Login(self,name,Acct_Number):
        self.cursor.execute("Select * From tbl_customer where name='"+name+"'")
        result1 = self.cursor.fetchone()
        if result1 is not None:
            self.cursor.execute("Select * From tbl_customer where Account_Number='"+Acct_Number+"'")
            result2 = self.cursor.fetchone()
            if result2 is not None:
                Auth = "success"
                print("Authentication Required!")
                if Auth == "success":
                    Email_Script_for_OTP.login.mail_login(Acct_Number)
                return True
            else:
                print("Account_Number is incorrect")
                return False
        else:
            print("User_name is Invalid ")
            return False

    def create_Account(self,name,initialdeposit,MailID,Phone_Number):
        self.name = name
        self.accountNumber = random.randint(10000, 99999)
        self.initialdeposit = initialdeposit
        self.MailID = MailID
        self.Phone_Number = Phone_Number
        Email_Script_for_OTP.login.mail_send_create(MailID)
        self.cursor.execute("Insert into tbl_customer(Name,Account_Number,Account_Balance)"
                            "values('" + self.name + "','" + str(self.accountNumber) + "','" + str(
            self.initialdeposit) + "')")
        self.cursor.execute("Insert into tbl_Contact_info(Account_Number,Email_ID,Phone_Number)"
                            "Values('" + str(self.accountNumber) + "','" + self.MailID + "','" + str(
            self.Phone_Number) + "')")
        self.db.commit()
        print("Account created successfully! Your Account Number is ",self.accountNumber)

    def displayBalance(self):
        self.name=name
        self.acctbal=self.cursor.execute("Select * From tbl_customer where name='"+name+"'")
        for row in self.acctbal:
            print("Your current Acctount Balane is ",row.Account_Balance)
        self.Account_Balance=row.Account_Balance

    def withdraw(self,withdraw_Amt):
        self.displayBalance()
        if withdraw_Amt<=self.Account_Balance:
            self.Account_Balance-=withdraw_Amt
            self.cursor.execute(
                "update tbl_customer set Account_Balance='"+str(self.Account_Balance)+"' where name='"+name+"'")
            self.db.commit()
            print("Withrawal Succesful,Your current Balance is ",self.Account_Balance)
        else:
            print("Insufficient Balance.")

    def deposit(self,deposit_Amt):
        self.displayBalance()
        self.Account_Balance += deposit_Amt
        self.cursor.execute(
            "update tbl_customer set Account_Balance='" + str(self.Account_Balance) + "' where name='"+name+"'")
        self.db.commit()
        print("Amount deposited Succesfully,Your current Balance is ", self.Account_Balance)
cust=Bank()
try:
    while True:
        print("1.Create Account")
        print("2.Login (Already Regiter)")
        print("3.Exit")
        print("Hi,Please Enter Any Number!")
        userchoice=int(input())
        if userchoice is 1:
            name = input("Enter Name :")
            initialdeposit = input("Enter deposit Amount :")
            MailID = input("Enter Your Mail_Id:")
            Phone_Number = int(input("Enter Your Phone Number:"))
            cust.create_Account(name, initialdeposit, MailID, Phone_Number)
        elif userchoice is 2:
            name =input("Enter Name :")
            Acct_Number=input("Enter Account_Number :")
            status=cust.Login(name,Acct_Number)
            if status is True:
                while True:
                    print("Hi,",name)
                    print("1.Withdraw")
                    print("2.Deposit")
                    print("3.Display_Balance")
                    print("4.Exit")
                    userchoice=int(input())
                    if userchoice is 1:
                        withdraw_Amt=int(input("Enter withdraw Amt:"))
                        cust.withdraw(withdraw_Amt)
                    elif userchoice is 2:
                        deposit_Amt=int(input("Enter deposit amt:"))
                        cust.deposit(deposit_Amt)
                    elif userchoice is 3:
                        cust.displayBalance()
                    elif userchoice is 4:
                        quit()
                    elif userchoice > 4 or userchoice <= 0:
                        print("Please enter Positive num below 4")
        elif userchoice is 3:
            quit()
        elif userchoice > 3 or userchoice <= 0:
            print("Please enter Positive num below 4")
except ValueError:
    print("please re-check the value entered!")
    print("Try again later!")
except Exception:
    print("Something went Wrong Please try again later!")

