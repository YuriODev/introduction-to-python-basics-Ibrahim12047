def get_new_number(number):
  num1 = number // 10000
  num2 = (number // 1000) % 10
  num3 = (number // 100) % 10
  num4 = (number // 10) % 10
  num5 = number % 10
  newnum_1 = num1 + num3 + num5
  newnum_2 = num2 + num4

  new_number = newnum_1 * 10 + newnum_2
  return new_number
new_number = get_new_number(int(input("Enter a five-digit number: ")))
print(new_number)