import os
class CustMgmt:
    def showAllcake(self):
        try:  
            with(open("cake.txt","r")) as fp:
               print(fp.read())
        except:  
            print("File does not exist.")     

    
    def searchById(self,id):
        try:
            with open("cake.txt","r") as fp:
                for line in fp:
                    try:
                        line.lower().index(str(id),0,4)
                        print("Found :",line)
                        break
                    except:
                        pass                        
                else:
                    print("Record not found")            
        except:
            print("File does not exist..")


    def addtocart_byid (self,id)  :
        allcake=[]
        found=False
        try:
            with(open("cake.txt","r")) as fp:
                for line in fp:
                    try:
                        line.lower().index(str(id),0,4)
                        with(open("customer.txt","a")) as fp:
                            pass
                    except:
                        pass
                    else:
                        found=True
                        line=line.split(",")
                        print(line)
                        line[3]=input("Enter cake quantity:")
                        line[3]+="\n"
                        line=",".join(line)
                        allcake.append(line)
            if(found):
                with(open("customer.txt","a")) as fp:
                    for i in allcake:
                        fp.write(i) 
                    print("Cake added to the cart.") 
            else:
                print("cake not found")
        except:
            print("File doesn't exist.")
            return                              
   
    def searchByName(self,name):
        try:
            with open("cake.txt","r") as fp:
                for line in fp:
                    try:
                        (line.lower()).index(name.lower())
                        print("Found :",line)
                        break
                    except:
                        pass                        
                else:
                    print("Record not found")            
        except:
            print("File does not exist..")
        
    def removeById(self,id):
        allCake = []
        found = False
        try:
            with open("customer.txt","r") as fp:
                for line in fp:
                    try:
                        line.lower().index(str(id),0,4)                        
                    except:
                        allCake.append(line)
                    else:
                        found = True
                  
        
            if(found):
                with open("customer.txt","w") as fp:
                    for x in allCake:
                        fp.write(x)
            else:
                print("Record not found")
        except:
            print("File is not present")
            return

    def showcart(self):
        try:
            with(open("customer.txt","r")) as fp:
                print(fp.read())
        except:
            print("File does not exist...")
            return  

    def buycake(self): 
        allcake=[]
        cakes = []
        sum = 0
        try:
            with(open("customer.txt","r")) as file:
                for line in file:
                    line = line.split(",")
                    cakes.append(line)
                    bill = float(line[2]) * int(line[3])
                    allcake.append(bill) 
                for k in allcake:
                    sum = sum + k 
            try:
                os.remove("customer.txt")
            except:
                print("File not found")
            else:
                print("\n______FINAL BILL______")
                print("cake ammount:Rs.",sum)
                gst = sum * (18/100)
                print("GST 18% of total:Rs.",gst)
                sgst = sum *(9/100)
                print("9% SGST on GST 18%:Rs.",sgst)
                cgst = sum *(9/100)
                print("9% CGST on GST 18%:Rs.",cgst)
                total = sum + gst
                print("Total bill:Rs.",total)
                print("Thank you....do visit again..")

                finalCakes = []
                with open("cake.txt","r") as fp:
                    for line in fp:
                        line = line.split(",")
                        for cake in cakes:
                            if(cake[0] == line[0]):
                                line[3] = str(int(line[3])-int(cake[3]))
                                line[3]+="\n"
                        line=",".join(line)        
                        finalCakes.append(line)
                 
                    
                    with open("cake.txt","w") as fp:
                        for r in finalCakes:
                            fp.write(r)    
        except:
            print("File does not exit")
                                          


    

    