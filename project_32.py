# How to find maximum number in a float number?
num = float(input('Enter number: '))
s_num = str(num)
maxi = -1
for i in range(len(s_num)):
    if s_num[i] == '.':
        continue
    elif maxi < int(s_num[i]):
        maxi = int(s_num[i])
print(f'Maximum digit is {maxi}.')
