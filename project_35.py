# printing alphabets from desired range.
start = input("Enter starting point:")
stop = input('Enter stopping point:')
while start != chr(ord(stop)+1):
    print(start, end=' ')
    start = chr(ord(start)+1)
print()
