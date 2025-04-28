import heapq


def a_star_search(grid, start, end, n):
    def manHattan(node):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

    def getNeighbors(node):
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] # up , down, left , right
        neighbors = []
        for move in moves:
            neighbor = (node[0] + move[0], node[1] + move[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n and grid[neighbor[0]][neighbor[1]] != 1:
                neighbors.append(neighbor)
        return neighbors

    path = [] # will store the nodes that we have traversed
    pq = []
    heapq.heappush(pq, (0 + manHattan(start), 0, start, [start]))  # sum, backward cost, cur_node, path list)

    visited = set() # will make sure we don't get into an infinite loop

    while pq:
        _, g, cur_pos, cur_path = heapq.heappop(pq)

        if cur_pos in visited: # avoid a already visited position. May occur when we get back due to an obstacle
            continue

        visited.add(cur_pos)
        path = cur_path  # Update the final path

        if cur_pos == end:
            return True, path
        neighbors = getNeighbors(cur_pos)
        for neighbor in neighbors:
            if neighbor not in visited:
                heapq.heappush(pq, (g + 1 + manHattan(neighbor), g + 1, neighbor, cur_path + [neighbor])) # assuming every move costs 1
                print(f"current node {cur_pos} and neighbor node {neighbor}. Path:")


    return False, []

n = int(input("Enter the row ,col of the maze (single value) : "))
maze = []
for i in range(n):
    row = []
    for j in range(n):
        temp = int(input(f"Enter the state of position [{i}][{j}]: "))
        row.append(temp)
    maze.append(row)
startx = int(input("Enter x coordinate of start node:"))
starty = int(input("Enter y coordinate of start node:"))
targetx = int(input("Enter x coordinate of target node:"))
targety = int(input("Enter y coordinate of target node:"))
start = (startx,starty)
target=(targetx,targety)
# maze = [
#     [0, 0, 1, 0, 0],
#     [0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 1],
#     [1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0]
# ]

start = (0, 0)
target = (4, 4)
res, path = a_star_search(maze, start, target, len(maze))

if res:
    print("Path found:", path)
else:
    print("Path not found")