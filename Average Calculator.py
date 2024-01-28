#This program calculates and displays the average of all the odd numbers between 40 and 240.



number_count = 0
sum = 0

for number in range (40, 240):
  if number % 2 != 0:
    number_count += 1
    sum += number
print("The average of all the odd numbers between 40 and 240 is", str(sum/number_count) + ".")