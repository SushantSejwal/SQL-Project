def purchase(user):
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

    if f"{user}PURCHASE" not in custTable:
        custExecuter.execute(f"""
            CREATE TABLE {user}PURCHASE (
                name VARCHAR(30),
                category VARCHAR(30),
                price INT
            );
        """)
        databaseConsumer.commit()

    # Purchasing Product
    dataTable = ['CPU', 'CPU_COOLER', 'MOTHERBOARD', 'MEMORY', 'STORAGE',
        'GPU', 'PSU', 'CABINET', 'MONITOR'
    ]

    categoryDict = {}


    def category():
        print("\n\nchoose one Categories to buy available Products")
        for num, category in enumerate(dataTable):
            if category == 'CPU_COOLER':
                print(f"  {num} for : CPU COOLER")
                categoryDict[num] = category
            else:
                print(f"  {num} for : {category}")
                categoryDict[num] = category
    category()

    # loop running flag
    flag = "Locomotives are amazing"
    while flag:
        price = 0
        choosedProductList = []
        choosingDict = {}

        choose = input(" -->   ")
        if choose.isdigit() :
            choose = int(str(choose))
            if choose in categoryDict.keys():
                for key in categoryDict.keys():
                    if choose == key:

                        dataExecuter.execute(f"SELECT * FROM {categoryDict[key]}")
                        products = dataExecuter.fetchall()

                        dataExecuter.execute(f"DESC {categoryDict[key]}")
                        productsDescList = dataExecuter.fetchall()
                        productsDesc = []
                        for i in productsDescList :
                            productsDesc.append(i[0])

                        print(f"\n   Available {categoryDict[key]} are :")
                        for num, product in enumerate(products):
                            choosingDict[num] = [product[0], categoryDict[key], product[-1]]
                            print(f"      {num} for : {product[0]}")
                            for i in range(len(productsDesc)):
                                if productsDesc[i] == "name":  pass

                                elif productsDesc[i] == "maxMemory":
                                    print(f"             Max Memory - {product[i]}")

                                elif productsDesc[i] == "refreshRate":
                                    print(f"             Refresh Rate - {product[i]}")

                                else: 
                                    productsDesc[i] = productsDesc[i].lower().strip().title()
                                    print(f"             {productsDesc[i]} - {product[i]}")
                            print()
                            sleep(0.1) # a little gap in next ouput

                        while True:
                            chooseProd = input("      -->  ")
                            if chooseProd.isdigit() :
                                chooseProd = int(str(chooseProd))
                                if chooseProd in choosingDict.keys():
                                    for key in choosingDict.keys():
                                        if chooseProd == key:
                                            choosedProductList.append(choosingDict[key][0])
                                            choosedProductList.append(choosingDict[key][1])
                                            choosedProductList.append(choosingDict[key][-1])
                                            price += choosingDict[key][-1]
                                            print(f"  product choose : {choosingDict[key][0]}")
                                            print(f"  price : ${price}")
                                            break
                                    break
                                else:
                                    print("choose only from available option")
                                    continue
                            else:
                                print("choose only from available option")
                                continue

                        custExecuter.execute(f"""
                            insert into {user}PURCHASE values
                            ("{choosedProductList[0]}", 
                            "{choosedProductList[1]}",
                            {price});
                        """)
                        databaseConsumer.commit()
                        print("\nitem has been add to cart\n")
                        break
            else:
                print("choose only from available option")
                continue
        else:
            print("choose only from available option")
            continue

        while True:
            again = input("do you wanna buy another Product ? [yes/no] :  ")
            again = again.lower().strip()

            if again =="yes" or again =="y":
                print()
                category()
                break

            elif again =="no" or again =="n":
                print("\n")
                flag = False
                break

            else:
                print("whoopse\n")

    custExecuter.close()
    dataExecuter.close()