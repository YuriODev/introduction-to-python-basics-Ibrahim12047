# Exercise 10
# Your solution comes here
def calculate_minute_angle(a):
  minute_degrees = (a % 30) * 12
  return minute_degrees
input_angle = float(input("Enter the angle by which the hour hand has turned since the beginning of the day: "))
minute_angle = calculate_minute_angle(input_angle)