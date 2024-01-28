#This program determines the largest prime factor of the number 600851475143.

number = 600851475143
potential_factor = 2 

while potential_factor * potential_factor < number:
  while number % potential_factor == 0:
    number /= potential_factor
  potential_factor += 1

print ('The largest prime factor of the number 600851475143 is', str(number) + '.')