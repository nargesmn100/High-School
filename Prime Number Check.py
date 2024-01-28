#This function takes a number as a parameter and checks if the number is prime or not.



def prime_check(number): 
	flag = True 
	for i in range(2,int(number/2)): 
		if number % i == 0: 
			flag=False 
			break 
	if flag: 
		return True #for prime 
	else: 
		return False #for not prime

num=int(input("Enter a number to check for it being prime: ")) 
if prime_check(num): 	
	print(num, "is a prime number.") 
else:
	print(num, "is not a prime number.") 
