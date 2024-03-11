import random 

print('number guess')
a = int(input('insert number1: '))
b = int(input('insert number1: '))
random_num = random.randint(a,b)

count = 0
guess = int(input(f'hads bezan adad bin {a},{b}: '))
flag = True
while flag:
    if guess < random_num:
        count += 1
        print(f'try {count}: kam goft dobareh telash kon: ')
        guess = int(input(f'hads bezan adad bin {a},{b}: '))
    elif guess > random_num:
            count += 1
            print(f'try {count}ziad goft dobareh telash kon: ')
            guess = int(input(f'hads bezan adad bin {a},{b}: '))
    else:
         count += 1
         print(f'shoma bad az {count} telash movvaq shodid adad {random_num} hads bezanid.')
         flag = False