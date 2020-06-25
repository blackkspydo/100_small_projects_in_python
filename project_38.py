# How to sort words according to their length?
s = ' '
s_words = input("Enter your words:")
words = list(s_words.split())
sorted_word = sorted(words, key=len)
print(s.join(sorted_word))
# method second
x = ' '.join(str(i) for i in sorted_word)
print(x)
