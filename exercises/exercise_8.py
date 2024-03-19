# Exercise 8
# Your solution comes here
def sort_three_integers(a, b, c):
  minimum = min(a, b, c)
  maximum = max(a, b, c)
  middle = (a + b + c) - minimum - maximum
  return (minimum, middle, maximum)
print(sort_three_integers(3, 1, 2))