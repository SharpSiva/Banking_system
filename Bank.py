import random
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
                print("Login successful")
                return True
            else:
                print("Incorrect Account_Number")
                return False
        else:
            print("Invalid User_name")
            return False

    def create_Account(self,name,initialdeposit):
        self.name = name
        self.accountNumber = random.randint(10000, 99999)
        self.initialdeposit = initialdeposit
        self.cursor.execute("Insert into tbl_customer(Name,Account_Number,Account_Balance)"
                            "values('" + self.name + "','" + str(self.accountNumber) + "','" + str(
            self.initialdeposit) + "')")
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

while True:
    print("1.Create Account")
    print("2.Login (Already Regiter)")
    print("3.Exit")
    print("Hi,Please Enter Any Number!")
    userchoice=int(input())
    if userchoice is 1:
        name = input("Enter Name :")
        initialdeposit = input("Enter deposit Amount :")
        cust.create_Account(name,initialdeposit)
    elif userchoice is 2:
        name =input("Enter Name :")
        Acct_Number=input("Enter Account_Number :")
        status=cust.Login(name,Acct_Number)
        if status is True:
            while True:
                print("Vanakam ,",name)
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
    elif userchoice is 3:
        quit()
