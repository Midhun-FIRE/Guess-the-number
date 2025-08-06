import random
y = random.randint(1,100)
c = 0
while True:
    try:
        x = int(input('Enter a number : '))
    except ValueError:
            print('Invalid Input')
            continue
    if x == y:
        c += 1
        print(f'congrats You got the answer in {c} attempts')
        print('''
        NEXT ROUND
        ''')
        
        y = random.randint(1,100)
        c = 0
    elif x > y :
        print('you guessed high')
        c += 1
    else:
        print('You guessed too low')
        c += 1
