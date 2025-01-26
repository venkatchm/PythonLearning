from datetime import datetime

def timeNow() -> None: # or we can write def timeNow():
    #print("Time now is :" datetime.now()) #invalid syntax use f string or separate print statement
    print(f'time now is : {datetime.now()}')
    print('Time now is: ')
    print(datetime.now())



timeNow()