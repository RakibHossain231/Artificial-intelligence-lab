
import random
import math

def execute_hill_climbing(points, origin, point_count):

    def get_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def path_total_cost(path, points):
        cost = 0.0
        length = len(path)
        for i in range(length):
            cost += get_distance(points[path[i-1]], points[path[i]])
        return cost

    tour = list(range(point_count))
    tour.append(0)
    tour_cost = path_total_cost(tour, points)

    while True:
        m, n = random.sample(range(1, point_count), 2)
        new_tour = tour.copy()
        new_tour[m], new_tour[n] = new_tour[n], new_tour[m]
        new_cost = path_total_cost(new_tour, points)

        if new_cost < tour_cost:
            tour, tour_cost = new_tour, new_cost
        else:
            break

    return tour_cost, tour


# Input section
location_count = int(input("Enter number of locations: "))
points_list = []
print("Enter coordinates for location")

for num in range(location_count):
    x_coord, y_coord = map(int, input().split())
    points_list.append((x_coord, y_coord))

start_point = points_list[0]

result_cost, result_path = execute_hill_climbing(points_list, start_point, location_count)

print("Path: ", end=" ")
path_size = len(result_path)
for idx in range(path_size):
    if idx != path_size - 1:
        print("", result_path[idx] + 1, end="->")
    else:
        print(result_path[idx] + 1)
print("Cost for this path is:", round(result_cost, 2))
