import time
from itertools import groupby
#raw_input = input("$ ")
time_list = []
for i in range(10):
    raw_input = "MMDCCCLXXXVIII 50"
    start = time.time()

    roman_num, iterations = raw_input.split(" ")[0], raw_input.split(" ")[1]

    counting = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"] #roman counting
    split_numeral = []
    #for i in range(int(iterations)):
    not_temp_list = []
    for i in range(int(iterations)):
        not_temp_list = [] #not_temp_list = [''.join(g) for _, g in groupby(roman_num)]
        temp_string = ""
        for i in range(len(roman_num)-1):
            #split into groups of like letters
            if roman_num[i] != roman_num[i+1]:
                temp_string = temp_string + roman_num[i]
                not_temp_list.append(temp_string)
                temp_string = ""
                if i == len(roman_num)-2:
                    temp_string = temp_string + roman_num[i+1]
                    not_temp_list.append(temp_string)
            else:
                temp_string = temp_string + roman_num[i]
                if i == len(roman_num)-2:
                    temp_string = temp_string + roman_num[i+1]
                    not_temp_list.append(temp_string)

        roman_num = ""

        for i in not_temp_list:
            temp_string = ""
            temp_string = counting[len(i)-1] + i[0]
            #print(temp_string)
            #print(roman_num)
            roman_num = roman_num+temp_string


    print(roman_num.count("I"))
    print(roman_num.count("V"))

    time_list.append(time.time() - start)

for i in time_list:
    print(i)
        
