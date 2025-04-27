def hillClimbing(maze, start,end, maxIteration):
    def manhattanFunction(node):
        return abs(node[0]-end[0])+abs(node[1]- end[1]);
    
    def getNeighbor(node):
        neighbors=[]
        moves= [(0,1), (1,0), (0,-1), (-1,0)] # (0,1)→right, (1,0)→down, (0,-1)→left, (-1,0)→up
        # increase means right and down
        # decrease means left and up
        for move in moves:
            neighbor= (node[0]+move[0], node[1]+move[1])
            if(0<=neighbor[0]<=4 and 0<=neighbor[1]<=4 and maze[neighbor[0]][neighbor[1]]!=1):
                neighbors.append(neighbor)    
        return neighbors;
    
    currentNode=start
    path=[currentNode]
    for _ in range(maxIteration):
        if currentNode==end:
            return path, True
        neighbors= getNeighbor(currentNode)
        
        bestNeighbor= min(neighbors, key=manhattanFunction)
        if manhattanFunction(bestNeighbor)>= manhattanFunction(currentNode):
            return path, False
        else:
            currentNode=bestNeighbor
            path.append(currentNode)
    return path, False
    
        



maze= [
    [0,1,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,1,0,1,1],
    [0,1,0,0,0]
]

start= (0,0)
end= (4,4)
maxIteration= 100 # if loop runs 100 times but we don't find the goal then lopp will be stope
path, result= hillClimbing( maze, start, end, maxIteration)
print(result, path)