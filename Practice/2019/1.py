import math
import time
inp = input()
start = time.time()

def isPalindrome(test_case):
    if test_case == test_case[::-1]:
        return True
    else:
        return False
def find_palindrome():
    if len(inp.strip())%2 == 0:#checks if number is even
        mid_point = len(inp)//2
        palindrome = inp[:mid_point]+inp[:mid_point][::-1]
        if int(palindrome) <= int(inp):
            mid_num = int(palindrome[mid_point-1])
            palindrome = palindrome[:mid_point-1] + str(mid_num+1) + str(mid_num+1) + palindrome[mid_point+1:]
        print(palindrome)
    else:
        split_point = math.ceil(len(inp)/2)-1
        middle_index = math.floor(len(inp)/2)
        palindrome = inp[:split_point] + inp[middle_index] + inp[:split_point][::-1]
        if (int(palindrome) <= int(inp)):
            if int(inp[middle_index])+1 > 9:
                palindrome = inp[:split_point-1] + str(int(inp[middle_index-1])+1) + "0" + str(int(inp[middle_index-1])+1) + inp[:split_point-1][::-1]
                if not isPalindrome(palindrome):
                    found = False
                    counter = 1
                    while not found:
                        curr = int(inp) + counter
                        if str(curr) == str(curr)[::-1]:
                            print(curr)
                            found = True
                            return
                        counter += 1

            else:
                palindrome = inp[:split_point] + str(int(inp[middle_index])+1) + inp[:split_point][::-1]
        print(palindrome)

    print(time.time() - start)

find_palindrome()



#!doesn't run in under a second for larger numbers
#inp = int(input("$ "))
#
#found = False
#counter = 1
#while not found:
#    curr = inp + counter
#    if str(curr) == str(curr)[::-1]:
#        print(curr)
#        found = True
#        break
#    counter += 1