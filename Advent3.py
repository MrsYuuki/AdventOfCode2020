def open_file(file_name):
    map = []
    file = open(file_name, "r")
    line = file.readline()
    while line!="":
        n_line = line.replace("\n", "")
        new_tab = []
        for i in n_line:
            new_tab.append(i)
        map.append(new_tab)
        line = file.readline()
    return map

def route_check(map, add_x, add_y):
    trees = 0
    x = 0
    y = 0
    while y != len(map) - 1:
        x += add_x
        x = x % len(map[y])
        y += add_y
        if map[y][x] == "#":
            trees += 1
    return trees

map = open_file("Advent3.txt")

multiple_trees = route_check(map, 3, 1)

for i,j in [[1,1], [5,1], [7,1], [1,2]]:
    multiple_trees = multiple_trees * route_check(map, i, j)

print(multiple_trees)
