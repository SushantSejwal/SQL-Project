def builder(user):
    import mysql.connector as sql
    from time import sleep

    # database contaning all the data
    databaseSushant = sql.connect(
        host = "localhost", 
        user = "root",
        password = "progress",
        database = "sushant"
    )
    # database in which data will store
    databaseConsumer = sql.connect(
        host = "localhost", 
        user = "root",
        password = "progress",
        database = "consumer"
    )
    dataExecuter = databaseSushant.cursor()
    custExecuter = databaseConsumer.cursor()

    custExecuter.execute("SHOW tables;")
    custTableList = custExecuter.fetchall()
    custTable = []
    for i in custTableList :
        custTable.append(i[0])

    if f"{user}CUSTOM" not in custTable:
        custExecuter.execute(f"""
            CREATE TABLE {user}CUSTOM (
                CPU varchar(30),
                COOLER varchar(30),
                MOTHERBOARD varchar(30),
                MEMORY varchar(30),
                STORAGE varchar(30),
                GPU varchar(30),
                PSU varchar(30),
                CABINET varchar(30),
                MONITOR varchar(30),
                PRICE int
            );
        """)
        databaseConsumer.commit()



    # ==***== CHOOSING PRODUCTS ==***== #
    # product tables
    dataTable = ['CPU', 'CPU_COOLER', 'MOTHERBOARD', 'MEMORY', 'STORAGE',
        'GPU', 'PSU', 'CABINET', 'MONITOR'
    ]
    choosedProductList = []
    price = 0

    for item in dataTable:
        dataExecuter.execute(f"SELECT * FROM {item}")
        products = dataExecuter.fetchall()

        dataExecuter.execute(f"DESC {item}")
        productsDescList = dataExecuter.fetchall()
        productsDesc = []
        for i in productsDescList :
            productsDesc.append(i[0])

        choosingDict = {}


        print(f"\n\n   Choosing {item}")
        for num, product in enumerate(products):
            print(f"     {num} for : {product[0]} + ${product[-1]}")
            choosingDict[num] = [product[0], product[-1]]

            for i in range(len(productsDesc)):
                if productsDesc[i] == "name" or productsDesc[i] == "price": pass

                elif productsDesc[i] == "maxMemory":
                    print(f"               Max Memory - {product[i]}")

                elif productsDesc[i] == "refreshRate":
                    print(f"               Refresh Rate - {product[i]}")

                elif productsDesc[i] == "price":
                    print(f"               {productsDesc[i]} - ${product[i]}")

                else: 
                    productsDesc[i] = productsDesc[i].lower().strip().title()
                    print(f"               {productsDesc[i]} - {product[i]}")
            print()
            sleep(0.1) # a little gap in next ouput

        while True:

            choose = input(" -->   ")

            if choose.isdigit() :
                choose = int(str(choose))
                if choose in choosingDict.keys():
                    for key in choosingDict.keys():
                        if choose == key:
                            choosedProductList.append(choosingDict[key][0])
                            price += choosingDict[key][-1]
                            print(f"  product choose : {choosingDict[key][0]}")
                            print(f"  total price : ${price}")
                            break
                    break
                else:
                    print("choose only from available option")
                    continue
            else:
                print("choose only from available option")
                continue

    custExecuter.execute(f"""
        insert into {user}CUSTOM values
        ("{choosedProductList[0]}", "{choosedProductList[1]}", "{choosedProductList[2]}",
        "{choosedProductList[3]}", "{choosedProductList[4]}", "{choosedProductList[5]}",
        "{choosedProductList[6]}", "{choosedProductList[7]}", "{choosedProductList[8]}",
        {price});
    """)
    databaseConsumer.commit()
    print("\nPC has been add to cart\n\n")

    custExecuter.close()
    dataExecuter.close()