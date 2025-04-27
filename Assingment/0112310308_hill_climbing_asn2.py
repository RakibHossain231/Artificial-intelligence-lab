import random
import math

def hill_climbing(locations, warehouse, numberOFLocations):

    def euclidean_distance(a, b): # Find out Euclidean distance between two locations
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def total_distance_for_A_Route(route, locations):
        distance = 0.0
        lengthOfRoute= len(route)
        for i in range(lengthOfRoute):
            distance += euclidean_distance(locations[route[i-1]], locations[route[i]]) # find out the locations coordinate using index ( route[i]= index)
        return distance


    current_route = list(range(0,numberOFLocations)) # mainly here we get the index list of locations between 0 to all locations
    current_route = current_route + [0]  # add warehouse at end
    current_distance = total_distance_for_A_Route(current_route, locations)
    
    while True:
        
        i, j = random.sample(range(1, numberOFLocations), 2) # Generate neighbor by swapping two non-warehouse nodes for the different route create
        new_route = current_route.copy() # assume current route is new route
         
        new_route[i], new_route[j] = new_route[j], new_route[i] # Swap two node for make new route
        new_distance = total_distance_for_A_Route(new_route, locations) # find the new route distance
        
        if new_distance < current_distance: # if new route is better then swap to current route and new route
            current_route, current_distance = new_route, new_distance
        else:
            break
    
    return current_distance, current_route


# Input
N = int(input("Enter number of locations: "))
locations= [] # (0, 0), (2,3), (4,0),(4,3), (6,1)
for x in range (N):
    print("Enter the Coordinate for location-> ", x+1,end =": ")
    x,y= map(int, input().split());
    p= (x,y);
    locations.append(p);
    
warehouse= locations[0]
  
cost, path= hill_climbing(locations, warehouse, N)

print("Path: ",end=" ")
lengthOfPath= len(path)
for x in range(lengthOfPath): # for keep the output formate same
    if(x!=lengthOfPath-1):
        print("", path[x]+1, end="->")
    else:
        print(path[x]+1)
print("Cost for this path is: ", round(cost,2))