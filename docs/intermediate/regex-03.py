import re
my_input = '1'

# check for one or more digits
digits_test = re.search('^\d+', my_input)

if digits_test:
  print("We have one or more digits!")
else:
  print("Invalid data")