#This program takes a list from the user and prints True if there is any element that appears more than once, it does not modify the original list.



print("Let us determine if your list includes repeating elements.")
empty_list = []
input_number = int(input('Enter the number of individual elements you wish for your list to have:  '))

for number in range(input_number):
  element = input("Enter your element: ")
  empty_list.append(element)
if input_number <= 0:
  print('Thank you for using my program.')
elif len(empty_list) != len(set(empty_list)):
  print("True; (at least) one element in your list is being repeated.")
else:
  print("False; none of the elements in your list are being repeated. ")
