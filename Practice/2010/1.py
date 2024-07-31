inp = input("$ ")
factor_list = []
for i in range(8):
    if i == 0: continue
    if sorted(list(inp)) == sorted(list(str((int(inp)*(i+1))))):
        factor_list.append(str(i+1))

if factor_list == []: print("NO")
else: print(" ".join(factor_list))