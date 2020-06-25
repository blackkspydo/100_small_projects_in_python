# How to make a Binary search of number in array.
def search(data, element):
    l = 0
    u = len(data) - 1

    while l <= u:
        mid = (l + u) // 2
        if data[mid] == element:
            globals()['pos'] = mid
            return True
        else:
            if data[mid] < element:
                l = mid + 1
            else:
                u = mid - 1
    return False
s = 'I am a disco dancer'
data = list(s.split(' '))
#data = sorted(data)
print (data)
element = 'a'
if search(data, element):
    print(element, 'found at position', pos + 1)
else:
    print(element, 'not found in data.')


