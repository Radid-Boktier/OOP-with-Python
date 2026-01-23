#Create a Class
class Item:
  pay_rate = 0.8
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
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate
  
#create instance of a class
item1 = Item('Phone',100,3)
item2 = Item('Laptop',1000,2)

print(Item.pay_rate)
#First check instance level if not find then go class level for attributes
print(item1.pay_rate)
print(item2.pay_rate)

print(Item.__dict__) #All the attributes for class level 
print(item1.__dict__) #All the attributes for instance level


item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7;
item2.apply_discount();
print(item2.price)



