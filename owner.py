from cake import Cake
from cakemgmt import Cakemgmt

def owner():
    choice = 0
    cakemgmt = Cakemgmt()
    while(choice != 6):
        print("\t\t1.Add a cake")
        print("\t\t2.Search a cake")
        print("\t\t3.Edit a cake")
        print("\t\t4.Delete a cake")
        print("\t\t5.Show all cakes")
        print("\t\t6.Exit")
        choice = int(input("Enter your choice:"))
        if(choice == 1):
            eid = int(input("Enter the cake id:"))
            ename = input("Enter the cake name:")
            eprice = int(input("Enter the cake price:"))
            equantity = int(input("Enter the cake quantity:"))
            e2 = Cake(eid,ename,eprice,equantity)
            cakemgmt.addcake(e2)

        elif(choice == 2):
            print("\ta.Search cake by id:")
            print("\tb.Search cake by name:")
            ch = input("Enter your choice (a or b):")
            if(ch.lower() == "a"):
                id =int(input("Enter the  cake id to search:"))
                cakemgmt.search_by_id(id)
            elif(ch.lower() == "b"):
                name = input("Enter cake name to search:")
                cakemgmt.search_by_name(name)
            else:
                print("Invalid choice")

        elif(choice == 3):
            id = int(input("Enter the id you want to edit:"))
            cakemgmt.edit_by_id(id)

        elif(choice == 4):
            id = int(input("Enter the id you want to delete:"))
            cakemgmt.delete_by_id(id)

        elif(choice == 5):
            cakemgmt.showallcake()

        elif(choice == 6):
            pass
        else:
            print("Invalid choice")
        
