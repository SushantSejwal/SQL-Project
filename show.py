def showProduct():
    import mysql.connector as sql
    from time import sleep

    # database contaning all the data
    database = sql.connect(
        host = "localhost", 
        user = "root",
        password = "progress",
        database = "sushant"
    )
    executer = database.cursor()

    tables = ['CPU', 'CPU_COOLER', 'MOTHERBOARD', 'MEMORY', 'STORAGE',
        'GPU', 'PSU', 'CABINET', 'MONITOR' ]
    categoryDict = {}

    def category():
        print("\n\nchoose from Categories to see available Product")
        for num, category in enumerate(tables):
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
        choose = input(" -->   ")
        if choose.isdigit() :
            choose = int(str(choose))
            if choose in categoryDict.keys():
                for key in categoryDict.keys():
                    if choose == key:

                        executer.execute(f"SELECT * FROM {categoryDict[key]}")
                        products = executer.fetchall()

                        executer.execute(f"DESC {categoryDict[key]}")
                        productsDescList = executer.fetchall()
                        productsDesc = []
                        for i in productsDescList :
                            productsDesc.append(i[0])

                        print(f"\n   Available {categoryDict[key]} are :")
                        for num, product in enumerate(products):
                            print(f"      {num}. {product[0]}")
                            for i in range(len(productsDesc)):
                                if productsDesc[i] == "name":  pass

                                elif productsDesc[i] == "maxMemory":
                                    print(f"        Max Memory - {product[i]}")

                                elif productsDesc[i] == "refreshRate":
                                    print(f"        Refresh Rate - {product[i]}")

                                elif productsDesc[i] == "price":
                                    print(f"        {productsDesc[i]} - ${product[i]}")

                                else: 
                                    productsDesc[i] = productsDesc[i].lower().strip().title()
                                    print(f"        {productsDesc[i]} - {product[i]}")
                            print()
                            sleep(0.1) # a little gap in next ouput
                        break
            else:
                print("choose only from available option")
                continue
        else:
            print("choose only from available option")
            continue

        while True:
            again = input("do you wanna see product from another category ? [yes/no] :  ")
            again = again.lower().strip()

            if again =="yes" or again =="y":
                category()
                break

            elif again =="no" or again =="n":
                print("\n")
                flag = False
                break

            else:
                print("whoopse\n")