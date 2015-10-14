def plural(number, words):

    if ((number % 100 != 11) & ((number % 10) == 1)):
        print(number, ''.join(words[0]))
    elif(((4 < number % 100 < 21) == False) & (1 < (number % 100) < 5)):
        print(number, ''.join(words[1]))
    else:
        print(number, ''.join(words[2]))


word = input()
number = int(input())

if word == "утюг":
    words = ["утюг", "утюга", "утюгов"]
elif word == "ложка":
    words = ["ложка", "ложки", "ложек"]
elif word == "гармошка":
    words = ["гармошка", "гармошки", "гармошек"]
elif word == "чайник":
    words = ["чайник", "чайника", "чайников"]


plural(number, words)
