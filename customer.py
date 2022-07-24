from cakemgmt import Cakemgmt
from custmgmt import CustMgmt

def customer():
    print("The user menu:")
    choice = 0
    cakemgmt=Cakemgmt()
    custMgmt = CustMgmt()
    while(choice != 7):
        print("\t\t1.View all cakes")
        print("\t\t2.Search a cake")
        print("\t\t3 Add to cart")
        print("\t\t4. Remove a cake from cart")
        print("\t\t5. Show cart ")
        print("\t\t6. Buy a cake")
        print("\t\t7.Exit")
        choice = int(input("Enter your choice:"))
        if(choice == 1):
            try:
                with(open("cake.txt","r")) as fp:
                    print(fp.read())
            except:
                print("File does not exist...")
                return
            
           
        elif(choice == 2):
            print("\ta.Search a cake by id:")
            print("\tb.Search a cake by name:")
            ch = input("Enter your choice (a or b):")
            if(ch.lower() == "a"):
                id =int(input("Enter a cake id to search:"))
                cakemgmt.searchByid(id)
            elif(ch.lower() == "b"):
                name = input("Enter a cake name to search:")
                cakemgmt.searchByname(name)
            else:
                print("Invalid choice")

        elif(choice == 3):
            id = int(input("Enter the id you want to add to cart:"))
            custMgmt.addtocart_byid(id)

        elif(choice == 4):
            id = int(input("Enter a cake id to remove:"))
            custMgmt.removeById(id)

        elif(choice == 5):
            custMgmt.showcart()

        elif(choice == 6):
            custMgmt.buycake()

        elif(choice == 7) : 
            print("Invalid choice")
        
