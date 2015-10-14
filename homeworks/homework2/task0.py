def plural(number, words):

    if ((number % 100 != 11) & ((number % 10) == 1)):
        return(words[0])
    elif(((4 < number % 100 < 21) == False) & (1 < (number % 100) < 5)):
        return(words[1])
    else:
        return(words[2])


word = input()
number = int(input())

if word == "����":
    words = ["����", "�����", "������"]
elif word == "�����":
    words = ["�����", "�����", "�����"]
elif word == "��������":
    words = ["��������", "��������", "��������"]
elif word == "������":
    words = ["������", "�������", "��������"]


print(number, plural(number, words))
