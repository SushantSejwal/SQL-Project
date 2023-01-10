def total(user):    
    
    import mysql.connector as sql
    from time import sleep

    # checking table exist or not
    databaseSS = sql.connect(
        host = "localhost", 
        user = "root",
        password = "progress",
        database = "sushant"
    )
    ssExecuter = databaseSS.cursor()
    ssExecuter.execute("SHOW tables;")
    tableList = ssExecuter.fetchall()
    tables = []
    for i in tableList :
        tables.append(i[0])
    if f"{user}CUSTOM" in tables:
        pass
    else:
        print("\n\ncart is empty\n\n")
        return

    # database in which data will store
    databaseConsumer = sql.connect(
        host = "localhost", 
        user = "root",
        password = "progress",
        database = "consumer"
    )
    executer = databaseConsumer.cursor()

    executer.execute(f"SELECT * FROM {user}CUSTOM;")
    customData = executer.fetchall()

    executer.execute(f"SELECT * FROM {user}PURCHASE;")
    purchaseData = executer.fetchall()

    total = 0

    for i in customData:
        total += i[-1]

    for i in purchaseData:
        total += i[-1]

    print(f"\n\ntotal price of items in cart : ${total}\n\n")

    executer.close()