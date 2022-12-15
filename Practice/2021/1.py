aplphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string = input("$ ")
s1, s2, comb = string.split(" ")[0], string.split(" ")[1], string.replace(" ", "")

if len(s1) == 1 and len(s2) == 1:
    print("YES")
    print("YES")