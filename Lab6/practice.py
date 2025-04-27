import math
def hillClimbing(maze, start, goal, mxIterations):
    
    def heuristics(node):
        return abs(goal[0]-node[0])+abs(goal[1]-node[1])
    
    def getNeighbor(node):
        neighbors=[]
        moves= [(0,1), (1,0), (0,-1), (-1,0)]
        
        for x in moves:
            neighbor= (x[0]+node[0], x[1]+node[1])
            if 0<=neighbor[0]<=4 and 0<=neighbor[1]<=4 and maze[neighbor[0]][neighbor[1]]!=1:
                neighbors.append(neighbor)
        return neighbors
    
    currentNode= start
    path= [currentNode]
    
    for _ in range(mxIterations):
        if(currentNode==goal):
            return True, path
        
        neighbors= getNeighbor(currentNode)
        bestNeighbor= min(neighbors, key=heuristics)
        
        if heuristics(bestNeighbor)>= heuristics(currentNode):
            return False, path
        else:
            currentNode= bestNeighbor
            path.append(currentNode)
    return False, path
        


#==== Main ====

maze= [
    [0,1,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,1,0,1,1],
    [0,1,0,0,0]
]

start=(0,0)
goal= (4,2)
mxIterations= 100
result, path= hillClimbing(maze, start,goal, mxIterations)
print(result)
print(path)