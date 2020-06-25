# How to check if the string is palindrome.
word = input('Enter any word: ')
r_word = word[::-1]
if word.lower() == r_word.lower():
    print(f'{word} is a Palindrome.')
else:
    print(f'{word} is not a Palindrome.')
