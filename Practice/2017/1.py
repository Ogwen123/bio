import time
import random
from functools import lru_cache

inp = input("$ ")
inp = "RRRRRGGBGGRRGBRGBRGBGBRRRRBRRBGBGGRRGRBGRGBBRRGRGGRRBGGRGBRRBBGBBGBBGGGRRRRBGRGGRRRRGRRRRGRGRBBGBBRGRRRGBRGGGRGGGRGGGRBBRGGBRRRRGBGGBGGBRBRBRGBGGRRBRRRGBGGRGBRRBBBGGGRRRGGBRRBGBBGGGBBRBRGGGBBGRBBGBRRRGGRGGGBRBBGRRBBGGGRBBBRRRBBBBRGRBRGRRGBRBBBBGGBGGGGRBRBRBRGBBGGGRBGGGGRRRGRBBGBRGRBRBBGBRGRBGGRBBBBGRBGBRBBRRBBRRGGBRGBRGBBBBGBGGBBBGGGGGGRBRGGRBBBRBRBGBBGRBBGGGBRRRBRGGGBRBRBGGRGBGGRRRGGRBGRRRBRGGGBGBGBRRGGRRGBGGBRGRBBBGGGRGGBRGGRBGBBGBGRRRGRRBBRRGGBBBRRGGGBRGRBRBRBRBGGGBBRGGGGGGRBBBRGGRRGRBRRRGBGGBGGGGGBBRRRRGGGRRRBBRBBGBBGRGGRGRBBBBRRBRRBRBRRGGGGBBGBBGRRRGRRRGBGGRBBGRBGBGBRRGRBBRBRGGRBRGBBGGBBBRRRBBGGBBRBBGGGBBBRGRGRGRRRBBBGGGRBBGBBBBGGBRBGGBGBRBGBGBGGRRBGRRRRRBBGGBRRRBGGBGGGBRBRGBRGBGRGRRGBRBRGBBRBRBGBBRGGRGBGBRGRRBRBRRBBBBGRRBBGRGBBGGGBBBRRBBRRBRBGBRRRBGBGRBBRGRBBBGRBRRRBGBBGRGGRBBGGBRGGBRBRGGGBGGBBGBGGBRGBGGRGGGGBRBBRRRRGGBGBRBGBRBBRRBGBBGGRRBGGGRRRRRGRGGGGBRGRGBBGGBBGRBRBRGGGBGGBRGBBGRBRGBRRGGBRBGGRBRRBRRBGBBBBGBRGGRRBRGGRRGBGRRRBRRRBRBBBBGRGBGGGRRGGGBRBGBBBBRGBRGRGBGRRGRBBGRRBBGGBR"
start = time.time()
data = list(inp)
rows = []
rows.append(data)
letters = ["R", "G", "B"]
#for i in range(1000):
#    string = string + letters[random.randint(0, 2)]
#print(string)
@lru_cache(maxsize=64)
def simulate_triangle():
    for i in range(len(data)):
        temp = []
        cur = rows[-1]
        for j in range(len(cur)-1):
            if cur[j] == cur[j+1]:
                temp.append(cur[j])
            else:
                global letters
                del letters[letters.index(cur[j])]
                del letters[letters.index(cur[j+1])]
                temp.append(letters[0])
                letters = ["R", "G", "B"]
        rows.append(temp)

    #print(rows)

    print(rows[-2][0])
    print(time.time() - start)

simulate_triangle()
