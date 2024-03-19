# Exercise 11
# Your solution comes here
def calculate_bills(s):
  denominations = [500, 100, 10, 5, 2, 1]
  bills = []

  for denomination in denominations:
      count = s // denomination
      s = s % denomination
      bills.append(count)

  return bills
total_cost = int(input("Enter the total cost of the goods purchased: $"))
bill_counts = calculate_bills(total_cost)
