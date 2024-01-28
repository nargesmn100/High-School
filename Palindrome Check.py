#This program takes a single word from the user, and prints “Yes” if the word is a palindrome and “NO” otherwise.


user_word = input("Enter your possible palindrome here: ")
user_word = user_word.casefold()
rev_str = reversed(user_word)

def isPalindrome(s):
    return s == s[::-1]
ans = isPalindrome(user_word)
if ans:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")

# Note: A palindrome is a word that is spelled the same forwards and backwards.
