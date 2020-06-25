# How to create a temperature converter to convert both way?
temp = input("Insert any value of 'C' or 'F' : ")

unit = temp[-1]
temp = int(temp[0:-1])

if unit == 'C' or unit == 'c':
    temp = round(temp*(9/5)+32,2)
    print(str(temp) + 'F')
elif unit == 'F' or unit == 'f':
    temp = round((temp-32)*(5/9),2)
    print(str(temp) + 'C')