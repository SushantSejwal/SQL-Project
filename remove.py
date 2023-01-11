def remove(user):    
    
    import mysql.connector as sql
    from time import sleep


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


    def rmCustom():
        backUpdataList = []
        dataDict = {}
        print("\nCustom Builds\n")
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
            dataDict[num] = build
            print()
            sleep(0.1)
        print("choose from above to remove from custom build")   
        while True:
            choose = input("  -->   ")
            if choose.isdigit():
                choose = int(choose)
                if choose in dataDict.keys():
                    for key in dataDict.keys():
                        if choose == key:
                            pass
                        else:
                            backUpdataList.append(dataDict[key])
                    break
                else:
                    print("choose only from available option")
                    continue
            else:
                print("choose only from available option")
                continue
        executer.execute(f"DELETE FROM {user}CUSTOM")
        for dataTup in backUpdataList:
            executer.execute(f"""
                insert into {user}CUSTOM values
                ("{dataTup[0]}", "{dataTup[1]}", "{dataTup[2]}", "{dataTup[3]}", 
                "{dataTup[4]}", "{dataTup[5]}", "{dataTup[6]}", "{dataTup[7]}", 
                "{dataTup[8]}", {dataTup[9]});
            """)
        databaseConsumer.commit()
        print("Custom build has been removed")



    def rmIndividual():
        backUpdataList = []
        dataDict = {}
        print("\nIndividual PC Parts\n")
        for num, build in enumerate(purchaseData):
            print(f"    Item no. {num}")   
            print(f"       Name     - {build[0]}")
            print(f"       Category - {build[1]}")
            print(f"       Price    - ${build[2]}")
            dataDict[num] = build
            print()
            sleep(0.1)
        print("choose from above item number to remove ")   
        while True:
            choose = input("  -->   ")
            if choose.isdigit():
                choose = int(choose)
                if choose in dataDict.keys():
                    for key in dataDict.keys():
                        if choose == key:
                            pass
                        else:
                            backUpdataList.append(dataDict[key])
                    break
                else:
                    print("choose only from available option")
                    continue
            else:
                print("choose only from available option")
                continue
        executer.execute(f"DELETE FROM {user}PURCHASE")
        for dataTup in backUpdataList:
            executer.execute(f"""
                insert into {user}PURCHASE values
                ("{dataTup[0]}", "{dataTup[1]}", "{dataTup[2]}");
            """)
        databaseConsumer.commit()
        print("Item has been removed")
        

    print("\n\ndo wanna remove item from Custom build or Individual Parts")
    print(" Enter 1 for : Custom Build PC")
    print(" Enter 2 for : Individual PC Parts")
    print(" Enter 3 for : Leave")
    while True:
        customOrIndi = input("  -->   ")
        if customOrIndi.isdigit():
            customOrIndi = int(customOrIndi)

            if customOrIndi == 1:
                rmCustom()
                print("\n")
                break
                
            elif customOrIndi == 2:
                rmIndividual()
                print("\n")
                break

            elif customOrIndi == 3:
                print("\n")
                break

            else:
                print("choose only from available option")
                continue
        else:
            print("choose only from available option")
            continue