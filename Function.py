from datetime import datetime

def timeNow() -> None: # or we can write def timeNow():
    #print("Time now is :" datetime.now()) #invalid syntax use f string or separate print statement
    print(f'time now is : {datetime.now()}')
    print('Time now is: ')
    print(datetime.now())



timeNow()


def add(a: float, b: float) -> float: 
    return a + b

def sub(a: float, b: float):  # specifying return type is not mantatory 
    return a - b


print(add(4.0, 4.2))
print(sub(5.0, 4.2))