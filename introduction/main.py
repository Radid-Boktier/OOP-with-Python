#Create a Class
class Item:
  def calculate_total_price(self,x,y):
    return x*y
  
#create instance of a class
item1 = Item()

#assign attributes
item1.name = 'Phone'
item1.price = 100
item1.quantity = 3

#calling methods from instances of a class
print(item1.calculate_total_price(item1.price,item1.quantity))

#create instance of a class
item2 = Item()

#assign attributes
item2.name = 'Phone'
item2.price = 100
item2.quantity = 3

#calling methods from instances of a class
print(item1.calculate_total_price(item1.price,item1.quantity))