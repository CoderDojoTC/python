import re
my_input = 'a@myco.com'

# check for one or more digits
if re.search('^\w+@\w+\.\w+$', my_input):
  print("E-mail address valid")
else:
  print("Error: Invalid email address!")