from itertools import permutations
import time
inp = input("$ ")
start = time.time()
num, start_string = inp.split(" ")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

permutations = ["".join(p) for p in permutations(alphabet[0:int(num)])]

matching = 0
for i in range(len(permutations)):
    if permutations[i].startswith(start_string):
        matching += 1

print(matching)
print(time.time() - start)