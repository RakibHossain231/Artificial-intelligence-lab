import random
import math

def simulated_annealing(locations, warehouse, max_iteration):
    def euclidean_distance(a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def total_distance(route, locations):
        distance = 0.0
        for i in range(len(route)):
            distance += euclidean_distance(locations[route[i-1]], locations[route[i]])
        return distance

    N = len(locations)
    current_route = list(range(N))
    current_route.remove(0)  # Remove warehouse (index 0)
    current_route = [0] + current_route + [0]  # Start and end at warehouse
    
    current_distance = total_distance(current_route, locations)
    while max_iteration!=0:
    
        # Generate neighbor by swapping two non-warehouse nodes
        i= random.sample(range(1, N), 1)
        neighbor_route = current_route.copy()
        
        neighbor_distance = total_distance(neighbor_route, locations)
        
        if neighbor_distance < current_distance:
            current_route, current_distance = neighbor_route, neighbor_distance
        max_iteration-=1
    return current_distance, current_route



#n = int(input("Enter number of locations: "))
locations= [(0, 0), (2,3), (4,0),(4,3), (6,1)]
# for x in range (n):
#     print("Enter the Coordinate for location-> ", x+1,end =": ")
#     x,y= map(int, input().split());
#     p= (x,y);
#     locations.append(p);
    
warehouse= locations[0]
max_iteration= 100
cost, path= simulated_annealing(locations, warehouse, max_iteration)
print("Path is: ", path)
print("Cost for this path is: ", cost)