class Shopper:
    def __init__(self,name):
        self.name=name
        self.grocery_list=[]
    
class Grocery_items:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
shopper1=Shopper("John")
shopper2=Shopper("Jane")
item1=Grocery_items("Milk", 2.99)
item2=Grocery_items("Bread", 1.99)
item3=Grocery_items("Eggs", 3.99)

shopper1.grocery_list.append(item1)
shopper2.grocery_list.append(item1)
 
for item in shopper1.grocery_list:
    print(shopper1.name,item.name, item.price)
for item in shopper2.grocery_list:
    print( shopper2.name ,item.name, item.price)