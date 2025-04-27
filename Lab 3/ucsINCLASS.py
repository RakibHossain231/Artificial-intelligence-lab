
import heapq

def dijkstra(graph, startNode):
    pq= []
    heapq.heappush(pq, (0, startNode)) # we push in heap distance and node


    distances= dict()
    for node in graph:
        distances[node]= float('inf') # distances= {node: float('inf') for node in graph}
    distances[startNode]=0


    visited= set()
    for x in graph:
        visited.add(float('inf'))
        
    parent= dict()
    for x in graph:
        parent[x]= None

    while pq:
        distance, currentNode=heapq.heappop(pq)
        if currentNode in visited:
            continue
        else:
            visited.add(currentNode)

        for neighbor, weight in graph[currentNode].items():
            tempDistance= weight+distance
            if tempDistance<distances[neighbor]:
                distances[neighbor]= tempDistance
                parent[neighbor]= currentNode
                heapq.heappush(pq, (tempDistance, neighbor))
    return distances, parent;





graph= { 
    'A':{'B': 1, 'C':4},
    'B':{'A':1, 'C':2, 'D':6},
    'C':{'A': 4, 'B':2, 'D':3},
    'D':{'B': 6, 'C':3}
}

startNode= 'A'
answer, parent=dijkstra(graph, startNode)

print(answer)

goal_Node='D'
path= [goal_Node]
x=parent[goal_Node]
path.append(x)

while x!= startNode:
    x=parent[x]
    path.append(x)
print(path)