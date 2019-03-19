C, W = [int(s) for s in input().split()]

words = input().split()

maxlength = max([len(word)for word in words])

printLength = maxlength
if printLength % 2 == 0:
    printLength += 1

print("* " * int(( printLength + 4) /2 ) + "* ")

while len(words) > 0:
    print("* ", end="")
    length = 0
    paddingLength = length
    word_on_line = False
    while len(words) > 0:
        word = words[0]
        length += len(word)
        if word_on_line:
            length += 1

        if length <= maxlength:
            words.pop(0)
            paddingLength = length
            print(word, end=" ")
            word_on_line = True
        else:
            break

    print (" " * (printLength - paddingLength ), end="")
    print("*")

print("* " * int(( printLength + 4) /2) + "* ")