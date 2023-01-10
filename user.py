import mysql.connector as sql

database = sql.connect(
    host = "localhost", 
    user = "root",
    password = "progress"             
)
executer = database.cursor()

# *** checking database exist or not *** #
executer.execute("SHOW databases;")
databaseList = executer.fetchall()
databases = []
for i in databaseList :
    databases.append(i[0])

if "consumer" in databases:
    executer.close()
    database = sql.connect(
        host = "localhost", 
        user = "root",
        password = "progress",
        database = "consumer"
    )
    executer = database.cursor()
else:
    executer.execute("CREATE DATABASE consumer;")
    database.commit()
    executer.close()
    database = sql.connect(
        host = "localhost", 
        user = "root",
        password = "progress",
        database = "consumer"
    )
    executer = database.cursor()

# *** checking table exist or not *** #
executer.execute("SHOW tables;")
tableList = executer.fetchall()
tables = []
for i in tableList :
    tables.append(i[0])

if "ACCOUNTS" not in tables:
    executer.execute("""
        CREATE TABLE ACCOUNTS (
            username varchar(35) not null PRIMARY KEY,
            password varchar(15) not null
        );
    """)
    database.commit()

executer.execute("SELECT * FROM ACCOUNTS")
userData = executer.fetchall()

def createAccount():
    while True:
        userName = input("Enter your username :  ")
        password = input(f"Enter password for {userName} (max 15 char):  ")
        sure = input(f"\n  User Name : {userName}\n  Password : {password} \
  \nare you sure these values are correct  ? [yes/NO] default(NO) :  ")
  
        if sure == "y" or sure == "yes":
            executer.execute(f"""
                insert into ACCOUNTS values
                    ("{userName}", "{password}")
            """)
            database.commit()
            print("account created")
            break
        else:
            print("\n\n")
            continue

    return(userName, password, True)



# ===***===*** sure ***===***=== #
def userLogin():

    
    while True :
    
        logIn = input("do you have a account resistered ? [yes/no] :  ")
        logIn = logIn.lower().strip()
        accountFound = False
        accountCreated = False

        if logIn == "y" or logIn == "yes":
            userName = input("Enter your username :  ")
            password = input(f"Enter password for {userName} :  ")
            for data in userData:
                if userName == data[0] and password == data[1]:
                    returningName = data[0]
                    returningPassword = data[1]
                    accountFound = True
                    accountCreated = True
                    break
            else:
                print("whopse, account not found\n")
                createChoice = input("Would you like to create new account ? [yes/no] :  ")
                createChoice = createChoice.lower().strip()

                if createChoice == "yes" or createChoice == "y":
                    returningName, returningPassword, accountCreated = createAccount()
                    break

                elif createChoice == "no" or createChoice == "n":
                    returningName = None
                    returningPassword = None
                    accountCreated = False
                    break

            if accountFound :
                break   
            
        elif logIn == "no" or logIn == "n":
            createChoice = input("Would you like to create new account ? [yes/no] :  ")
            createChoice = createChoice.lower().strip()

            if createChoice == "yes" or createChoice == "y":
                returningName, returningPassword, accountCreated = createAccount()
                break

            elif createChoice == "no" or createChoice == "n":
                returningName = None
                returningPassword = None
                accountCreated = False
                break


    return (returningName, returningPassword, accountCreated)