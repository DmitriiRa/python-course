name = input()
number = int(input())
if name == 'утюг':
    if (4 < (number % 100) < 21):
        print(number, 'утюгов')
    elif ((number % 10) == 1):
        print(number, 'утюг')
    elif (1 < (number % 10) < 5):
        print(number, 'утюга')
    else:
        print(number, 'утюгов')    
elif name == 'ложка':
    if (4 < (number % 100) < 21):
        print(number, 'ложек')
    elif ((number % 10) == 1):
        print(number, 'ложка')
    elif (1 < (number % 10) < 5):
        print(number, 'ложки')
    else:
        print(number, 'ложек') 
