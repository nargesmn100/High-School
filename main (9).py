#This function prints out the first n rows of Pascal's triangle. 



def printPascal(n) : 
    for line in range(0, n) : 
        for i in range(0, line + 1) : 
            print(binomialCoeff(line, i), 
                " ", end = "") 
        print() 
      
def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res 

user_number = int(input("How many rows of Pascal's triangle would you like to view? "))
n = user_number + 1
printPascal(n)