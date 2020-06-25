# How to build a simple calculator?
print('Zero terminates calculator')
while True:
    operator = input('\nEnter operator you need(+,-,*,/): ')
    try:
        if operator == '+':
            x, y = [int(i) for i in input('\nEnter your operation: ').split('+')]
            result = x + y

        elif operator == '-':
            x, y = [int(i) for i in input('\nEnter your operation: ').split('-')]
            result = x - y

        elif operator == '*':
            x, y = [int(i) for i in input('\nEnter your operation: ').split('*')]
            result = x * y

        elif operator == '/':
            x, y = [int(i) for i in input('\nEnter your operation: ').split('/')]
            result = x / y

        print(x, operator, y,'=', result)
    except:
        print('\n--------ERROR----------'
              '\n* Enter valid operators only '
              '\n* Do not use 0 as divisor'
              '\n* Enter full operation like a+b,a-b,a*b,a/b')
