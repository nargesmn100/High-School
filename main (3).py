#This function generates Fibonacci numbers to the amount which the user desires. 

def recur_fibo(n):
  if n <= 1:
    return n
  else:
    return(recur_fibo(n-1) + recur_fibo(n-2))

user_number = int(input("Please enter the amount of Fibonacci numbers you would like to view: "))

# check if the number of terms is valid
if user_number <= 0:
  print("Plese enter a positive integer")
else:
  print("\nHere are the first", user_number, "numbers in the Fibonacci sequence: ")
  for i in range(user_number):
    print(recur_fibo(i))

#Note: The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...