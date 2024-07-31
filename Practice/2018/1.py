import time
inp = input("$ ")

start = time.time()

debt_per, repay = int(inp.split(" "))
debt = 100

repay_count = 0

while debt > 0:
    print("--------------------")
    print(f"debt before: {debt}")
    debt = round(debt + (debt*(debt_per/100)), 2)
    print(f"debt: {debt}")
    repay_val = round(debt*(repay/100), 2)
    print(f"repay val: {repay_val}")
    if repay_val >= 50:
        debt -= repay_val
        repay_count += repay_val
        print("used repay val")
    else:
        if debt > 50:
            debt -= 50
            repay_count += 50
            print("print used 50")
        else:
            repay_count += debt
            debt -= debt
            print("used debt")

print(f"repay count: {repay_count}")