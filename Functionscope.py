
def myFunc():
    global name
    name = 'venkat'
    print(name)


def twoFunc():
    global name
    name = 'chalam'
    print(name)

myFunc()
twoFunc()
print(name)


def enterInput():
    print('enter input ')
    number = input()
    try:
        if int(number) < 3:
            print('less that 3')
        else: 
            print('greater than 3')
    except ValueError:
        print('random error')

enterInput()