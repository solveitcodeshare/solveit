#3 desperately dire deck deathra
# run with e.g. python p3_2018_carddeck.py  3
import sys
from collections import deque
deck = [x for x in range(int(sys.argv[1]))]
results = deque([])
while len(deck)>0:
    if len(results) > 0 : results.append(results.popleft())
    results.append(deck.pop())
for r in reversed(results): print(r,end=" ")
