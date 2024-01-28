#This function calculates the factorial of a number.



def factorial(user_number):
    if user_number == 0:
        return 1
    else:
        return user_number * factorial(user_number-1)

user_number = int(input("Enter a number to determine its factiorial: "))

print("The factorial of your number is " + str(factorial(user_number)) + ".")