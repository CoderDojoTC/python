import re
my_input = '1234'

# check to for exactly four digits
digits_test = re.search('^\d\d\d\d$', my_input)

if digits_test:
  print("We have exactly four digits!")
else:
  print("Invalid data")