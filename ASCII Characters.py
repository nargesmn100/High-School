#This program displays all the ASCII characters from 0 to 255 (numbers and corresponding ASCII values) in a visually pleasing format.



for number in range (256):
    ch = chr(number)
    print(number, "=\t" + ch)
print("\nTask completed successfully.")