def plural(number, words):

    if ((number % 100 != 11) & ((number % 10) == 1)):
        print(number, words[0])
    elif((4 < number % 100 < 21) == False & (1 < (number % 100) < 5)):
        print(number, words[1])
    else:
        print(number, words[2])


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


plural(number, words)
