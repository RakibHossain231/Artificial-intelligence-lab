import heapq

def aStarSearch(grid, start, end, n):
    def manhattan_Heuristic(x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def getNeighbor(node): # returns valid neighbors in the grid
        neighbors = []
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        for move in moves:
            neighbor = (node[0] + move[0], node[1] + move[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n and grid[neighbor[0]][neighbor[1]] == 0:
                neighbors.append(neighbor)
        return neighbors

    priorityQ = []
    heapq.heappush(priorityQ, (0, start))  # (f_score, node)

    parent = {}  # To reconstruct the shortest path
    g_score = {start: 0}  # Start node cost is 0
    f_score = {start: manhattan_Heuristic(start, end)}

    while priorityQ:
        dis, currentNode = heapq.heappop(priorityQ)

        if currentNode == end:  # Goal reached
            path = []
            while currentNode in parent:
                path.append(currentNode)
                currentNode = parent[currentNode]
            path.append(start)
            path.reverse()
            return True, path  # Return reversed path
        NEighbor= getNeighbor(currentNode)
        for neighbor in NEighbor:
            temp_g_score = g_score[currentNode] + 1  # Cost from start

            if temp_g_score+manhattan_Heuristic(neighbor,end) <= g_score[currentNode]+ manhattan_Heuristic(currentNode, end):  # If new path is better
                parent[neighbor] = currentNode  # Track path
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + manhattan_Heuristic(neighbor, end)
                heapq.heappush(priorityQ, (f_score[neighbor], neighbor))

    return False, None  # No path found


# Define the maze
# grid = [
#     [0,1,0,0,0],
#     [0,1,1,0,0],
#     [0,0,0,1,1],
#     [0,1,0,1,1],
#     [0,1,0,0,0]
# ]

n= int(input("Enter grid size: "))
grid = [[0] * n for _ in range(n)]

print("Enter the values of grid: ")
for i in range (n):
    for j in range (n):
        grid[i][j]= int(input())       

start_x, start_y = map(int, input("Enter start point: ").split())
start=(start_x, start_y)

end_x, end_y = map(int, input("Enter the goal point: ").split())
end= (end_x, end_y)

result, path = aStarSearch(grid, start, end, n)

print(result, end= ", ")
if result==True:
    print("Shortest Path:", path)
else:
    print("None")