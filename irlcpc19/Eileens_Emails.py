N = int(input())
lines = [input() for i in range(N)]

email_count = dict()
for line in lines:
    line = line.lower()
    email = ''
    for char in list(line):
        if char == ' ':
            email += '.'
        elif char > '`' and char < '{':
            email += char

    email_count[email] = email_count.get(email, 0) + 1

    if email_count[email] == 1:
        print("{}@ucc.ie".format(email))
    else:
        print("{}{}@ucc.ie".format(email, email_count[email]))












