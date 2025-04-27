import heapq
def ucs(graph, start, goal, H_Function):
    pq=[]
    heapq.heappush(pq, (0, start))
    
    distances= dict()
    for x in graph:
        distances[x]= float('inf')
        
    distances[start]=0

    
    parent= dict()
    for x in graph:
        parent[x]= None
    
    while pq:
        d, currentNode = heapq.heappop(pq)
        
        for neighbor, weight in graph[currentNode].items():
            tempDis= distances[currentNode]+ weight
            if tempDis < distances[neighbor]:
                distances[neighbor]= tempDis
                f_cost= tempDis + H_Function(neighbor, goal)
                parent[neighbor]= currentNode
                heapq.heappush(pq, (f_cost, neighbor))
    return distances, parent;

def heuristic_function(start, goal):
    map= {
        'a': {'d': 7},
        'b': {'d': 6},
        'c': {'d': 3},
        'd': {'d' : 0}
    }
    return map.get(start).get(goal)

def path(parent, start, goal):
    x= goal
    path=[x]
    while x!=start:
        x=parent[x]
        path.append(x)
    path.reverse()
    return path;
gp= {
    'a': {'b':1, 'c': 4},
    'b': {'a':1, 'd': 6, 'c': 2},
    'c': {'a': 4, 'b':2, 'd': 3},
    'd': {'b': 6, 'c': 3}
};
start= 'a'
goal= 'd'
dis, parent= ucs(gp, start, goal, heuristic_function)
ShortestPath= path(parent, start, goal)

print(dis)
print(ShortestPath)