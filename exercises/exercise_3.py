# Exercise 3
# Your solution comes here
n = int(input("Enter the number of seconds that have passed since the beginning of the day: ")) 
hours = n // 3600
minutes = (n % 3600) // 60
seconds = n % 60
print(hours,":",minutes,":",seconds)