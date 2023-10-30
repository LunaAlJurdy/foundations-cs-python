#Exercise 1

number=input("Enter a number")
print(len(number))
print()

#Exercise 2
n=int(input("Enter a number"))
for i in range (n):
    print("*"*(i+1))
    
print()

#Exercise 3
#list1=[54,76,2,4,98,100]
#int1=int(input("Enter a number"))
#Didn't know how to do it

#Exercise 4
Names=["maria","hala","ghady","ehsan","joe","zoe"]
letter=input("Enter a letter")
found_names=[name for name in Names if letter.lower() in name.lower()]
if found_names:
  print ("Names containing the letter:'{}'")
  for name in found_names:
    print(name)
else:
  print("No names containing the letter:'{}'")

