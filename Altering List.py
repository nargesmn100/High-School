#This program takes a list from the user and returns a new list that contains all but the first and last elements.



empty_list = []
sublist_number = int(input('State the number of sublists which you would like to have: '))

for number in range (sublist_number):
  element_number = int(input('How many elements would you like in this sublist? '))
  for numbers in range (0, element_number):
    all_elements = input("Please enter any element/character: ")
    empty_list.append(all_elements)
if sublist_number==1 and element_number == 1:
  empty_list.pop(0)
else:
  empty_list.pop(0)
  empty_list.pop(-1) 
print('Your list containing all but the first and last elements (which you have entered) is:', str(empty_list) + '.')