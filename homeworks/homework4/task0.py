with open("yazkora.txt") as f:
    sentences = f.read().split(".")
    answer = open("answer.txt", 'w')
    for sentence in sentences:
        words = sentence.replace('\n', ' ')
        words = sentence.split()
        for word in words:
            if word.endswith("yo"):
                word += ' '
                answer.write(word)
        answer.write('\n')
    answer.close()


# with open("answer.txt") as f:
#    for line in f:
#        print(line)