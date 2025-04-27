import heapq
def dijkstra(startNode, graph):
    visited = dict()
    for nd in graph:
        visited[nd] = 0
    pq = [] # will be used as a priority queue
    heapq.heappush(pq,(0,startNode)) # will be storing tuples here and priority is the distance
    distance = dict()
    for nd in graph:
        distance[nd] = float('inf')
    distance[startNode] = 0
    parent = dict()
    for nd in graph:
        parent[nd] = float('inf')
    while pq:
        current_dis, current_node = heapq.heappop(pq)
        if  visited[current_node] == 1:
            continue
        visited[current_node]  = 1
        for adjacent_node in graph[current_node]:
            if distance[current_node] + graph[current_node][adjacent_node] < distance[adjacent_node]:
                distance[adjacent_node] = distance[current_node] + graph[current_node][adjacent_node]
                heapq.heappush(pq,(distance[adjacent_node],adjacent_node))
                parent[adjacent_node] = current_node
    return parent

def path(parentArray, startnode, goalnode):
    if goalnode == startnode:
        print(f"{startnode} -> ",end="")
    else:
        path(parentArray,startnode,parentArray[goalnode])
        print(f"{goalnode} ->" , end="")
graph = {
    'a':{
        'b':1,
        'c':4
    },
    'b':{
        'a':1,
        'c':2,
        'd':6
    },
    'c':{
        'a':4,
        'b':2,
        'd':3
    },
    'd':{
        'b':6,
        'c':3
    }
};
startnode = 'a'
goalnode = 'd'
parent_array = dijkstra(startnode,graph)
print("Printing the Parent Array")
for nd in parent_array:
    print(f"{nd} : {parent_array[nd]}")
print("Printing the path for each node")
for nd in parent_array:
    print(f"Path for node {nd}")
    path(parent_array,startnode, nd)
    print()