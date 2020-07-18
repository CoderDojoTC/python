import re
my_input = 'a2'

# check for one or more digits
digits_test = re.search('^[a|b|c]\d$', my_input)

if digits_test:
  print("We a or b or c followed by a digit")
else:
  print("Invalid data")