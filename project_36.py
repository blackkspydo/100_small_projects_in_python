# How to replace substring from a string.
o_string = input('Enter your original string')
o_sub_string = input('Enter old substring to replace: ')
n_sub_string = input('Enter new sub string: ')
len_string = len(o_sub_string)


# find() returns lowest index of substring if found in string
i = o_string.find(o_sub_string)
string = o_string[:i] + n_sub_string + o_string[i + len_string:]

print(string)
