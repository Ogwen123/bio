import string
inp = input("$ ")

alphabet = list(string.ascii_uppercase)#ABCDEFGHIJKLMNOPQRSTUVWXYZ

final_string = ""
for i in range(len(inp)):
    idx = len(inp)-i-1
    if idx == 0:
        final_string = inp[0] + final_string
        continue
    final_string = alphabet[(alphabet.index(inp[idx]) - alphabet.index(inp[idx-1]))-1] + final_string

print(final_string)


