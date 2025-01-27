import random 

print('Welcome to guess the number')
print('===========================')
print('Please enter your guess number between 1 - 10')
myRandomNumber = random.randint(1, 10)
yourInput = input()
print(myRandomNumber)
try: 
    if int(yourInput) in range(1, 10): 
        print('closee  guess')
    else: 
        print('wrong guess')

except ValueError:
    print('invali error')

