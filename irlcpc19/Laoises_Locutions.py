N = int(input())

lines = [input() for i in range(N)]
results = []

for line in lines:
    counter = dict()
    line = line.lower()

    for char in list(line):
        if char > '`' and char < '{':
            counter[char] = counter.get(char, 0) + 1

    odds = 0
    for i in counter.values():
        if i % 2 == 1:
            odds += 1
            if odds == 2:
                break

    if odds >= 2:
        results.append("0")
    else:
        results.append("1")

print(" ".join(results))

