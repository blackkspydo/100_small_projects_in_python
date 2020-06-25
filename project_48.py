# How to check for file extension.
exe = ['gif', 'png', 'jpeg', 'jpg', 'txt', 'py']
file_exe = input('Enter you filename: ').split('.')
if len(file_exe) >= 2:
    extension = file_exe[-1]
    if extension in exe:
        print('File extension exists')
    else:
        print('File extension does not exist')
else:
    print('File has no extension')
