number = input("enter a number ") 
def new_number(number):

  num1 = number // 10000
  num2 = (number // 1000) % 10
  num3 = (number // 100) % 10
  num4 = (number // 10) % 10
  num5 = number % 10


  newnum_1 = num1 + num3 + num5
  newnum_2 = num2 + num4

 
  new_number = int(str(newnum_1) + str(newnum_2))

  return new_number

newnumber = new_number(number)
print(new_number)

