# This function creates a world matrix and initializes the starting point
# and destination and calls the find_safest_path function.
def main():
    world = [[1, 4, 1, 0],
            [1, 1, 0, 1],
            [0, 1, 1, 2],
            [0, 0, 1, 1]]
    N = len(world)
    start = (0, 0)
    destination = (N - 1, N - 1)
    path = [[0, 0, world[0][0]]]
    new_path = []
    find_safest_path(world, start, destination, path, new_path)


# This function takes the world matrix and the cell location (x and y) as parameters and
# returns true only if the cell is inside the world boundary and safe.
def is_safe(world, x, y):
    N = len(world)
    if 0 <= x < N and 0 <= y < N and world[x][y] != 0:
        return True
    else:
        return False

# This recursive function takes the world matrix, starting point,
# destination, list with starting point and its safety value, and global list as parameters and
# returns true if one or more safe paths are found; otherwise returns false.
# Also, this function saves all possible safe paths found to the global list.
def find_paths(world, start, destination, path, new_path):
    N = len(world)
    moved = [[False for j in range(N)] for i in range(N)]
    if start == destination:
        new_path.append(path[:])
        return True

    x,y = start
    moved[x][y] = True
    if is_safe(world, x, y):
        if y + 1 < N and (not moved[x][y + 1]):
            path.append([x, y + 1, world[x][y+1]])
            find_paths(world, (x, y + 1), destination, path, new_path)
            path.pop()

        if x + 1 < N and (not moved[x + 1][y]):
            path.append([x + 1, y,world[x+1][y]])
            find_paths(world, (x + 1, y), destination, path, new_path)
            path.pop()

    moved[x][y] = False

    return new_path

# This function takes the world matrix, starting point,
# destination, list with starting point and its safety value, and global list as parameters and
# calculate safety points for all paths and print the safest path as a world matrix if one
# or more safety path is found.
def find_safest_path(world, start, destination, path, new_path):
    N = len(world)
    if find_paths(world, start, destination, path, new_path):
        print("Safe paths: ")
        dictionary = {}
        for i in new_path:
            print(i)
            counter = 0
            for j in i:
                counter += j[2]

            dictionary[str(i)] = counter

        max_points = max(dictionary, key=dictionary.get)
        print()
        print(f"Safest path: {max_points} with safety points: {dictionary[max_points]}")
        print()
        new_list = []
        for i in new_path:
            if str(i) == max_points:
                new_list = i

        safe_matrix = [[0 for j in range(N)] for i in range(N)]
        for element in new_list:
            x = element[0]
            y = element[1]
            safe_matrix[x][y] = element[2]
        print("Safest path in the world:")
        for i in safe_matrix:
            for j in i:
                print(str(j) + " ", end="")
            print()

    else:
        print("This world is very dangerous, abort mission!!!")


main()







