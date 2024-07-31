import time
grid_inp = ""
dice = ["up", "6", "2"] # need to track: heading, touching grid, facing towards top
coords = [6, 6] #6, 6 = middle of the grid
for i in range(3):
    grid_inp = grid_inp + input(f"row {i+1}: ") + "\n"
start = time.time()
grid = [[1]*11 for i in range(11)]
temp_list = grid_inp.split("\n")
del temp_list[-1]
for i in range(len(temp_list)):
    grid[i+4][4] = int(list(temp_list[i].replace(" ", ""))[0])
    grid[i+4][5] = int(list(temp_list[i].replace(" ", ""))[1])
    grid[i+4][6] = int(list(temp_list[i].replace(" ", ""))[2])

print(grid)

do_loop = True
while do_loop:
    inp = int(input("enter num: "))
    if inp == 0:
        do_loop = False
        continue

    cur_grid_num = grid[(coords[1])-1][(coords[0])-1]
    cur_grid_num += inp
    while cur_grid_num > 6: cur_grid_num -= 6
    grid[(coords[1])-1][(coords[0])-1] = cur_grid_num
    if cur_grid_num in [1, 6]:
        if dice[0] == "up":
            if coords[1]-1 < 0: coords = [coords[0], coords[1]+10]
            else: coords = [coords[0], coords[1]-1]
        if dice[0] == "down":
            if coords[1]+1 > 10: coords = [coords[0], coords[1]-10]
            else: coords = [coords[0], coords[1]+1]
        if dice[0] == "left":
            if coords[0]+1 < 0: coords = [coords[0]-10, coords[1]]
            else: coords = [coords[0]-1, coords[1]]
        if dice[0] == "right":
            if coords[1]+1 > 10: coords = [coords[0]+10, coords[1]]
            else: coords = [coords[0]+1, coords[1]]
    print(coords)


    
    
