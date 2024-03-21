# Exercise 4
# Your solution comes here
number = input("enter a four-digit number: ")
if len(number)>4 :
  number=number+"0000"
if number[0] == number[3] and number[1] ==  number[2]:
  print("1")
else:
  print("0")