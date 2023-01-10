# importing time for some delay in output
from time import sleep

# importing modules to run the program
import user
import custom
import help
import show
import buy
import bag
import remove
import bill

# authentication step
userName, password, accoundExist = user.userLogin()
if accoundExist:
    print("\n\n**-***-***-*** WELCOME TO SUSHANT COMPUTER BULDER ***-***-***-**")
    print("              here you can build PCs and buy parts")

    print(f"\n\n              **-***-** Welcome  {userName} **-***-**\n")

# running program
while accoundExist:
    cmd = input("Enter command or type 'help' for help\n ->  ")
    cmd = cmd.lower().strip()
    sleep(0.1)

    if cmd == "help" or cmd =="h":
        help.commands()

    elif cmd == "custom":
        custom.builder(userName)

    elif cmd == "show":
        show.showProduct()

    elif cmd == "buy":
        buy.purchase(userName)

    elif cmd == "cart":
        bag.cart(userName)

    elif cmd == "rm":
        remove.remove(userName)

    elif cmd == "bill":
        bill.total(userName)

    elif cmd == "exit" or cmd == "e":
        exit()
    
    else:
        print("whoopse")
        print()

else:
    print("Login is required in order to proceed")