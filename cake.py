class Cake:
    def __init__(self,id,nm,price,equantity):
        self.eid= id
        self.ename = nm
        self.eprice = price
        self.equantity =equantity

    def __str__(self):
        return str(self.eid)+","+self.ename+","+str(self.eprice)+","+str(self.equantity)

    

    
