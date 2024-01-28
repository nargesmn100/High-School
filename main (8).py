#This function checks whether a number is perfect or not.



def perfect_number(user_number):
    sum = 0
    for i in range(1, user_number):
        if(user_number % i == 0):
            sum = sum + i
    return sum        

user_number = int(input("Please enter any number: "))

if user_number == perfect_number(user_number):
    print("%d is a perfect number." % user_number)
else:
    print("%d is not a perfect number." % user_number)