from customer import customer
from owner import owner

if(__name__ == "__main__"):
    print("\t\t1.Owner Menu")
    print("\t\t2.Customer Menu")
    choice = int(input("Enter your choice:"))
    if(choice == 1):        
        owner()
    elif(choice == 2):
        customer()