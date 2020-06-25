# How to make question of random number?
import random
result = random.randint(1,20)
guess = None
while result != guess:
    guess = int(input('\nGuess any number between 1 and 20: '))
    if guess <=20:
        if result > guess:
            print('Your guess is smaller than result. guess little higher.')
            continue
        elif result < guess:
            print('Your guess is higher than result. Guess little lower.')
            continue
        else:
            break
    else:
        print('Please input number between 1 and 20 only.')
        continue
print('Congratulations You guessed correctly.')
