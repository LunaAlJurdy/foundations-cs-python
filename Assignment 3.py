items=[["tomato",1],["potato",2],["chocolate",3],["soap",0.5]] 

def addItem():
  print("Please enter the name of item you would like to add: ")
  item = str (input())
  print("Please enter the price of the item: ")
  price = float(input())
  items.append([item,price])
  print("Item added")

def checkTotal():
  
  
  print("Your total is: ")
  total= float(input())
  print(total)
  print("What would you like to do next?")

def addCoupon():
  print("The value of the coupon is: ")
  coupon=float(input())
  print("Your final_total is: ")
  final_total=total-coupon
  print(final_total)

def checkout():
  print(items)
  print(total)
  print(coupon)
  print(final_total)
  mainMenu()

def newOrder():
  choice=-99 # dummy value
  while choice !=4:
    print("Enter")
    print("1. to add an item")
    print("2. to check total")
    print("3. to add a coupon")
    print("4. to checkout")

    choice=int(input())

    if choice==1:
      addItem()
    elif choice ==2:
      checkTotal()
    elif choice ==3:
      addCoupon()
    elif choice ==4:
      checkout()
    else:
      print("ivalid input")

# Menus
def mainMenu():
  choice=-99 # dummy value
  while choice !=2:
    print("Enter")
    print("1. to start a new order")
    print("2. to close the program")

    choice=int(input())

    if choice==1:
      print("starting a new order...")
      newOrder()
    elif choice ==2:
      print("bye bye")
    else:
      print("ivalid input")


mainMenu()

