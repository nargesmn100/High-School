#This program continues asking for phrases and number of exclamation marks until the user enters a value of zero or less for the number of exclamation marks, it then ends.



phrase = input("What word/sentence would you like to see displayed? ")
display_amount = int(input("How many exclamation marks (!) would you like your line to have? "))
times = display_amount
ch = '!'
total = ""

while times > 0:
  for n in range (display_amount):
    total += ch
  print(phrase + total)
  phrase = input("What word/sentence would you like to see displayed? ")
  times = int(input("How many exclamation marks (!) would you like your line to have? "))
else:
  print("Thank you for using my program.")