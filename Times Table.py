#This program enables the user to specify which times table to print, it continues running until the user responds with a "no" to the question "Would you like to see another one?". 



number = int(input("What number's times table would you like to display? "))
print("Below is the Multiplication Table of:", number)

for n in range (1, 13):
  print(number, 'x', n, "=", number * n)
continue_confirmation = input("\nWould you like to see another one? (Yes/No) ").title()

while continue_confirmation != 'No':
  if continue_confirmation == 'Yes':
    number = int(input("What number's times table would you like to display? "))
    print("Below is the Multiplication Table of:", number)
    for n in range (1, 13):
      print(number, 'x', n, "=", number * n)
    continue_confirmation = input("\nWould you like to see another one? (Yes/No) ").title()
  else:
    continue_confirmation = input("\nWould you like to see another one? (Yes/No) ").title()
else:
    print("Thank you for using my program.")