
t = int(input("Enter the number of minutes Helen needs to sleep: "))
h = int(input("Enter the hour Helen goes to bed: "))
m = int(input("Enter the minute Helen goes to bed: "))

total_minutes = h * 60 + m + t
wake_up_hour = (total_minutes // 60) % 24
wake_up_minute = total_minutes % 60
print(wake_up_hour)
print(wake_up_minute)
