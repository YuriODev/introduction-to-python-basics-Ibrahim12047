# Exercise 9
# Your solution comes here
def calculate_hour_angle(h, m, s):
  hour_degrees = (h % 12 + m / 60 + s / 3600) * 30
  return hour_degrees
h = int(input("Enter hours passed: "))
m = int(input("Enter minutes passed: "))
s = int(input("Enter seconds passed: "))

hour_angle = calculate_hour_angle(h, m, s)

print("Angle by which the hour hand has turned: {:.2f} degrees".format(hour_angle))