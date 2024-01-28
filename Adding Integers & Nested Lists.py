#This program takes a list of lists of integers from the user, and adds up the elements from all of the nested lists.



numbers_list = []
sublist_number = int(input('How many sublists would you like to put inside your nested list? '))

for number in range (0, sublist_number):
  element_number = int(input('How many elements would you like in this sublist? '))
  for numbers in range (0, element_number):
    element_count = int(input('What would you like this element to be? '))
    numbers_list.append(element_count)
print('All numbers:', numbers_list)
print('The sum of all the numbers which you have entered is:', sum(numbers_list))