cities=["Beirut","Zahle","Jbeil","Tripoli","Akkar","Saida"]
driver={}
driver["alex"]=["Beirut","Zahle"]
driver["anthony"]=["Saida","Beirut","Jbeil","Tripoli","Akkar"]
driver["samir"]=["Beirut"]

def order():
  order=[]
  choice=-99 # dummy value
  while choice !=5:
    print("Enter")
    print("1. to add a city")
    print("2. to add a driver")
    print("3. to add city to a driver")
    print("4. to remove a city")
    print("5. to check package")

    choice=int(input())

    if choice==1:
      addCity()

    elif choice ==2:
      addDriver()

    elif choice ==3:
      addCityToDriver()
    elif choice ==4:
      removeCity()
    elif choice==5:
      checkPackage()
    else:
      print("ivalid input")

def addCity():
  print("please choose a city")
  city=str(input())
  for i in range(len(cities)):

    if city in cities:
     print("the city you chose is present: ",city)

    else:
      print("the city you chose is added: ",city)

      cities.append(city)
      return city

def addDriver():
  addDriver=[]
  choice=-99 # dummy value
  while choice !=4:
    print("Enter")
    print("1. for alex who will go to Beirut then Zahle")
    print("2. for anthony who will go to Saida then Beirut,Jbeil, Tripoli and lastly Akkar")
    print("3. for samir who will go to Beirut")
    print("4. to add a new driver")


    choice=int(input())

    if choice==1:
      print("Alex will be taking you to Beirut then Zahle")

    elif choice ==2:
      print("Anthony will take you to Saida then Beirut,Jbeil, Tripoli and lastly Akkar")

    elif choice ==3:
      print("Samir will take you to Beirut")
    elif choice ==4:
      
      new_driver=input("Enter the name of the driver you would like to add: ").title()
    else:
      print("Invalid Input")
    
  Route=input("please choose to which cities you would like to go in order: ")
  return Route
def addCityToDriver():
  your_driver=input("Write the name of te driver you want to add a city to: ").title()
  
  another_city=input("Enter the cities you would like to add: ").title()
  driver["your_driver"]=Route+another_city
  
def mainMenu():
  choice=-99 # dummy value
  while choice !=2:
    print("Welcome")
    print("Enter")
    print("1. to start")
    print("2. to quit")

    choice=int(input())

    if choice==1:
      print("Starting your request")
      order()
    elif choice ==2:
      print("bye bye")
    else:
      print("ivalid input")

mainMenu()

