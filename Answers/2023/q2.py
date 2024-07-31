print("---------------------\nName: Owen Jones \nSchool: Cardiff High School\n---------------------\n")
inp = list(input("pentominoes: "))


pentominoes = {
"F":[[2, 1], [3, 1], [1, 2], [2, 2], [2, 3]],
"G":[[1, 1], [2, 1], [2, 2], [3, 2], [2, 3]],
"I":[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
"L":[[1, 1], [1, 2], [1, 3], [1, 4], [2, 4]],
"J":[[2, 1], [2, 2], [2, 3], [2, 4], [1, 4]],
"N":[[2, 1], [2, 2], [1, 2], [1, 3], [1, 4]],
"M":[[1, 1], [1, 2], [2, 2], [2, 3], [2, 4]],
"P":[[1, 1], [2, 1], [1, 2], [2, 2], [1, 3]],
"Q":[[1, 1], [2, 1], [1, 2], [2, 2], [2, 3]],
"T":[[1, 1], [2, 1], [3, 1], [2, 2], [2, 3]],
"U":[[1, 1], [3, 1], [1, 2], [2, 2], [3, 2]],
"V":[[1, 1], [1, 2], [1, 3], [2, 3], [3, 3]],
"W":[[1, 1], [1, 2], [2, 2], [2, 3], [3, 3]],
"X":[[2, 1], [1, 2], [2, 2], [3, 2], [2, 3]],
"Z":[[1, 1], [1, 2], [2, 2], [2, 3], [3, 3]],
"S":[[2, 1], [3, 1], [2, 2], [1, 3], [2, 3]],
"Y":[[1, 2], [1, 2], [2, 2], [2, 3], [2, 4]],
"A":[[1, 1], [1, 2], [2, 2], [1, 3], [1, 4]],
}
    
pento_1 = pentominoes[inp[0]]
pento_2 = pentominoes[inp[1]]
pento_1_geom = [0, 0]
pento_2_geom = [0, 0]
for i in pento_1:
    if i[0] > pento_1_geom[0]: pento_1_geom[0] = i[0]
    if i[1] > pento_1_geom[1]: pento_1_geom[1] = i[1]

for i in pento_2:
    if i[0] > pento_2_geom[0]: pento_2_geom[0] = i[0]
    if i[1] > pento_2_geom[1]: pento_2_geom[1] = i[1]

possible_position_factors = [(pento_1_geom[1]+(2)), (pento_1_geom[0]+(2))]
pento_1_pos = [pento_1[0][0] + pento_2_geom[0], pento_1[0][1] + pento_2_geom[1]]#position of highest and left most square

shapes = 0
done_pos = {}
for i in range(possible_position_factors[0]):
    for j in range(possible_position_factors[1]):
        done = False
        #check for overlaps
        x = i
        y = j

        pento_2_squares = [
        [pento_2[0][0]+x, pento_2[0][1]+y], 
        [pento_2[1][0]+x, pento_2[1][1]+y], 
        [pento_2[2][0]+x, pento_2[2][1]+y], 
        [pento_2[3][0]+x, pento_2[3][1]+y],
        [pento_2[4][0]+x, pento_2[4][1]+y]
        ]

        for k in pento_1:
            if done: continue
            if k not in pento_2_squares:#if no overlap check if they are touching
                for l in pento_2_squares:
                    if l[0] == k[0] and l[1]+1 == k[1]:
                        shapes += 1
                        done = True
                    elif l[0] == k[0] and l[1]-1 == k[1]:
                        shapes += 1
                        done = True
                    elif l[0]+1 == k[0] and l[1] == k[1]:
                        shapes += 1
                        done = True
                    elif l[0]-1 == k[0] and l[1] == k[1]:
                        shapes += 1
                        done = True  
                        
print(shapes)

"""
*********
*********
*********
****--***
***--****
****-****
*********
*********
*********
"""








#for i in pentominoes:
#    curr_pento = pentominoes[i]
#    string = ""
#    cur = [1, 1]
#    for i in range(25):
#        if cur in curr_pento:
#            string = string + "-"
#        else:
#            string = string + "*"
#        
#    
#        if (i+1)%5 == 0:
#            string = string + "\n"
#            cur[0] = 1
#            cur[1] += 1
#        else:
#            cur[0] += 1
#    
#    print(string)

#grid = ""
#for i in range(pento_1_geom[1]+pento_2_geom[1]*2):
#    grid = grid + ("*"*(pento_1_geom[0]+(pento_2_geom[0]*2)) + "\n")
#print(grid)
