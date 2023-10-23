from collections import deque
from copy import deepcopy

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dli = [-1, 0, 1, 0 , -1, -1 , 1, 1]
dlj = [0, 1, 0, -1 , -1 , 1 , 1 , -1]

visited = []
path = []


def sameIsland(map, c1):
    if map[c1[1]][c1[0]] == 'L' and c1 not in visited:
        visited.append(c1)
        for k in range(4):
            sameIsland(map, (c1[0] + di[k], c1[1] + dj[k]))


from queue import Queue


def organize_coordinates_as_path(coordinates):
    if len(coordinates) < 2:
        return coordinates  # Nothing to organize

    # Find the nearest neighbor for the start point
    start = coordinates[0]
    coordinates.remove(start)
    path = [start]

    while len(coordinates) > 0:
        current_point = path[-1]
        min_distance = float('inf')
        nearest_neighbor = None

        for point in coordinates:
            distance = ((current_point[0] - point[0]) ** 2 + (current_point[1] - point[1]) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = point

        if nearest_neighbor:
            coordinates.remove(nearest_neighbor)
            path.append(nearest_neighbor)
        else:
            break

    return path

def lee_algorithm(grid, start, end):
    queue = deque()
    visited = set()
    distance = {start: 0}
    prev = {}

    queue.append(start)
    visited.add(start)

    while queue:
        cord = queue.popleft()
        for k in range(8):
            neighbor = (cord[0] + di[k], cord[1] + dj[k])
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[cord] + 1
                prev[neighbor] = cord
                queue.append(neighbor)

            if neighbor == end:
                return get_shortest_path(prev, start, end)

    return None


def checkPath(line):
    path = [[line[i], line[i + 1]] for i in range(len(line) - 1)]
    for move in path:
        for k in range(4):
            if [[move[0][0] + di[k], move[0][1] + dj[k]], [move[1][0] - di[k], move[1][1] - dj[k]]] in path:
                return False
    return True


def get_shortest_path(prev, start, end):
    path = []
    node = end

    while node != start:
        path.append(node)
        node = prev[node]

    path.append(start)
    path.reverse()

    return path


def createPath(coord, map):
    for k in range(8):
        neighbour = (coord[0] + dli[k], coord[1] + dlj[k])
        isCoutour = False
        for k in range(4):
            if (neighbour[0] + di[k], neighbour[1] + dj[k]) in visited:
                isCoutour = True
                break
        if isCoutour and neighbour not in path and map[neighbour[1]][neighbour[0]] ==  'W':
            path.append(neighbour)
            createPath(neighbour, map)
            break



def mapispeelcontur(map):
    margine = visited[-1]
    for k in range(4):
        neighbor = (margine[0] + di[k], margine[1] + dj[k])
        if map[neighbor[1]][neighbor[0]] ==  'W':
            path.clear()
            path.append(neighbor)
            createPath(neighbor, map)



def getcContur():
    s = set()
    for cord in visited:
        for k in range(4):
            neighbor = (cord[0] + di[k], cord[1] + dj[k])
            if neighbor not in visited:
                s.add(neighbor)
    return list(s)
def find_farthest_points(grid):
    max_row, max_col = len(grid), len(grid[0])
    max_distance_north, farthest_north = 0, (0, 0)
    max_distance_south, farthest_south = 0, (0, 0)
    max_distance_east, farthest_east = 0, (0, 0)
    max_distance_west, farthest_west = 0, (0, 0)

    for row in range(max_row):
        for col in range(max_col):
            if grid[row][col]:
                distance_north = row
                distance_south = max_row - 1 - row
                distance_east = max_col - 1 - col
                distance_west = col

                if distance_north > max_distance_north:
                    max_distance_north = distance_north
                    farthest_north = (row, col)

                if distance_south > max_distance_south:
                    max_distance_south = distance_south
                    farthest_south = (row, col)

                if distance_east > max_distance_east:
                    max_distance_east = distance_east
                    farthest_east = (row, col)

                if distance_west > max_distance_west:
                    max_distance_west = distance_west
                    farthest_west = (row, col)
    points = [farthest_north, farthest_south, farthest_east, farthest_west]
    return points


def form_sqaure(grid, farthest_points):
    x_values, y_values = zip(*farthest_points)
    min_x = min(x_values)
    max_x = max(x_values)
    min_y = min(y_values)
    max_y = max(y_values)

    contour_coordinates = []

    # Calculate the points along the top edge
    for x in range(min_x, max_x + 1):
        contour_coordinates.append((x, min_y))

    # Calculate the points along the right edge
    for y in range(min_y, max_y + 1):
        contour_coordinates.append((max_x, y))

    # Calculate the points along the bottom edge
    for x in range(max_x, min_x - 1, -1):
        contour_coordinates.append((x, max_y))

    # Calculate the points along the left edge
    for y in range(max_y, min_y - 1, -1):
        contour_coordinates.append((min_x, y))

    return contour_coordinates

def read(filename):
    with open(filename, "r") as f:
        side = int(f.readline()[:-1])
        map = [[0 for _ in range(side)] for _ in range(side)]
        for i in range(side):
            line = f.readline()[:-1]
            for j in range(side):
                map[i][j] = line[j]
        outputs = []
        input = int(f.readline()[:-1])
        for i in range(input):
            line = f.readline()[:-1]
            line = line.split(" ")
            c1 = tuple([int(c) for c in line[0].split(",")])
            # c2 = (int(c) for c in line[1].split(","))
            visited.clear()
            sameIsland(map, c1)
            mapispeelcontur(map)
            print(path)
           # sorted_coordinates = sorted(contur, key=lambda k: [k[0], k[1]])
            outputs.append(deepcopy(path))
        f.close()

    with open(filename[:-3] + ".out", "w") as f:
        for output in outputs:
            s = ""
            for cord in output:
                s = s + str(cord[0]) + ',' + str(cord[1]) + ' '
            s = s[:-1] + '\n'
            f.write(s)
        f.close()
    return outputs

print(read("level5_example.in"))
print(read("level5_3.in"))
print(read("level5_4.in"))
print(read("level5_5.in"))
