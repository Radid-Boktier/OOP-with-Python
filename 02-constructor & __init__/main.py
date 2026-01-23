#Create a Class
class Item:
  def __init__(self,name,price,quantity=0):
    #Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than or equal to zero"
    assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

    #Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_price(self):
    return self.price*self.quantity
  
#create instance of a class
item1 = Item('Phone',100,-3)

#calling methods from instances of a class
print(item1.calculate_total_price())

#create instance of a class
item2 = Item('Laptop',1000,1)

#calling methods from instances of a class
print(item2.calculate_total_price())