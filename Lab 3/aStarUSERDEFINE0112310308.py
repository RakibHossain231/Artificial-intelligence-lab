import heapq
def aStar(graph, startNode, goal, heuristic_Function):

    priorityQUEUE=[] # Create priority Queue
    heapq.heappush(priorityQUEUE, (0, startNode)) # insert into Priority Queue
    
    dis= dict()
    for x in graph: # initialize distance infinity
        dis[x]= float('inf')
    dis[startNode]=0

    parent = dict() # initialize parent None
    for x in graph:
        parent[x]= None

    while priorityQUEUE:
        _, currentNode= heapq.heappop(priorityQUEUE)
        
        for neighbor, wei in graph[currentNode].items(): # explore connected notes
            tempDis= dis[currentNode]+ wei
            if tempDis < dis[neighbor]:
                dis[neighbor] = tempDis
                f_cost= tempDis + heuristic_Function(neighbor, goal)
                parent[neighbor]= currentNode
                heapq.heappush(priorityQUEUE, (f_cost, neighbor))
    return dis, parent;

def shortestPath(parent, starNode, goalNode): # Path find
    x= goalNode
    path=[x]
    
    while starNode!=x:
        x= parent[x]
        path.append(x)       
    path.reverse()
    return path;

def  heuristic_map(value):
    heuristic_map=value;
    return heuristic_map;

def heuristic_function(node, goal):  # Heuristic value find
    heuristic_map = {
        'A': {'D': 7},
        'B': {'D': 6},
        'C': {'D': 2},
        'D': {'D': 0}
    }
    return heuristic_map.get(node).get(goal)

# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 6},
#     'C': {'A': 4, 'B': 2, 'D': 3},
#     'D': {'B': 6, 'C': 3}
# }

# print(f"Graph: {graph}")


# User inputs graph that means make dictiona
useDefineGraph= dict()
row= int(input("How many node: "))
for row in range(0, row):
    node= input("Enter node: ")[0].upper()
    elements= int(input(f"How many node are connected with {node}: "))
    connected= dict()
    
    for element in range(0, elements):
        connectedNode = input(f"Enter connected node {element+1}: ")[0].upper()
        connectedNode=connectedNode.upper()
        weight= int(input("Enter weight: "))
        connected[connectedNode]=weight;
    useDefineGraph[node]= connected
    

print(f"User Define Graph: {useDefineGraph}")

startNode= input("Enter Start Node: ")[0].upper()
goalNode= input("Enter Goal node: ")[0].upper()

Dist, parent= aStar(useDefineGraph, startNode, goalNode, heuristic_function)
print(f"Source to All nodes: {Dist}")
# print(parent)

s_Path= shortestPath(parent, startNode, goalNode)
print(f"Shortest path from {startNode} to {goalNode}: {s_Path}")
