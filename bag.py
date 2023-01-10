def cart(user):    

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

    if customData:
        print("\n\n  Custom Builds\n")
    for num, build in enumerate(customData):
        print(f"    custom build no. {num}")   
        print(f"       CPU         - {build[0]}")
        print(f"       Cooler      - {build[1]}")
        print(f"       Motherboard - {build[2]}")
        print(f"       Memory      - {build[3]}")
        print(f"       Storage     - {build[4]}")
        print(f"       GPU         - {build[5]}")
        print(f"       PSU         - {build[6]}")
        print(f"       Cabinet     - {build[7]}")
        print(f"       Monitor     - {build[8]}")
        print(f"       Price       - ${build[9]}")
        print()
        sleep(0.1)
    print()
    sleep(0.1)
    if purchaseData:
        print("\n  Individual PC parts\n\n")
    for num, item in enumerate(purchaseData):
        print(f"    item no. {num}")   
        print(f"       Name     - {item[0]}")
        print(f"       Category - {item[1]}")
        print(f"       Price    - ${item[2]}")
        print()
        sleep(0.1)