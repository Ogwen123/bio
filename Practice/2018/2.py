#encrypty thing
from functools import lru_cache
import time

inp = input("input(n space word):")
start = time.time()
n, word = inp.split(" ")
n = int(n)

@lru_cache(maxsize=1)
def generate():
    global n
    first_dial = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    second_dial = ""
    #generating second dial
    index_tracker = 0
    while len(second_dial) < 26:
        index_tracker += n-1
        #while index_tracker > len(first_dial)-1:
        #    index_tracker -= len(first_dial)
        index_tracker %= len(first_dial)
        second_dial = second_dial + first_dial[index_tracker]
        if index_tracker == len(first_dial)-1: first_dial = first_dial[:-1]
        else: first_dial = first_dial[:index_tracker] + first_dial[index_tracker+1:]
    return second_dial

second_dial = generate()

first_dial = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted_word = ""

#encrypting
second_dial_list = list(second_dial)
for i in word:
    encrypted_word = encrypted_word + second_dial_list[first_dial.index(i)]
    second_dial_list.append(second_dial_list[0])
    del second_dial_list[0]

print(second_dial[:6])
print(encrypted_word)
print(time.time() - start)

