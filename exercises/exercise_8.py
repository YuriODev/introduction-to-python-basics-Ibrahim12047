# Exercise 8
# Your solution comes here
a=input()
b=input()
c=input()
minimum = min(a, b, c)
maximum = max(a, b, c)
middle = (a + b + c) - minimum - maximum
sorted_numbers = (minimum, middle, maximum)
print(sorted_numbers)
