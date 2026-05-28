thisdict = { 
  1:"Cheeseburger",
  2:"Fries",
  3:"Soda",
  4:"Ice Cream",
  5:"Cookie"
}


def get_item(i):
   
   item = thisdict.get(i)
   return item

def welcome():
   print(thisdict)
   
welcome()

item = int(input("What would you like to order? "))  
print(get_item(item))