#This program takes a list as an input and prints True if the list is sorted in ascending order and False otherwise.



empty_list = []
input_number = int(input('Enter the number of individual elements you wish for your list to have:  '))

for number in range(input_number):
  print("Please insert numbers in the order which you wish to check.")
  element = input("Enter your element: ")
  empty_list.append(element)
if input_number <= 0:
  print('Thank you for using my program.')
elif empty_list == sorted(empty_list): 
  print("True, your list is in ascending order.")
else:
  print("False, your list is not in ascending order.")