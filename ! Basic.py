#This program asks the user for a phrase, and the number of exclamation marks they would like to have following that phrase, it then then outputs the phrase followed by the number of exclamation marks indicated by the user without any spaces between them.



phrase = input("What word/sentence would you like to see displayed? ")
times = int(input("How many exclamation marks (!) would you like your line to have? "))
ch = '!'
total = ""

for n in range (times):
  total += ch
print(phrase + total)