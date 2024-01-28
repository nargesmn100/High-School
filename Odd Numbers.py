#This program uses a for loop to create a list of all odd numbers from 1 to 20, it then prints the list of numbers.



odd_numbers_list = [ ]

for number in range (1,20,2):
  odd_numbers_list.append(number)
print(odd_numbers_list)