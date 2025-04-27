
import random
import math

def perform_simulated_annealing(coords, depot, total_points, start_temp, cooling_factor):

    def calc_distance(point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    def compute_path_cost(path, coords):
        total = 0.0
        path_len = len(path)
        for i in range(path_len):
            total += calc_distance(coords[path[i-1]], coords[path[i]])
        return total

    route = list(range(total_points))
    route.append(0)
    route_cost = compute_path_cost(route, coords)
    temp = start_temp

    while True:
        if temp <= 0.1:
            print("Temperature cooled down")
            break

        a, b = random.sample(range(1, total_points), 2)
        trial_route = route.copy()
        trial_route[a], trial_route[b] = trial_route[b], trial_route[a]
        trial_cost = compute_path_cost(trial_route, coords)

        change = trial_cost - route_cost
        if change < 0:
            route, route_cost = trial_route, trial_cost
        else:
            acceptance_chance = math.exp(-change / temp)
            if random.uniform(0, 1) <= acceptance_chance:
                route, route_cost = trial_route, trial_cost

        temp *= cooling_factor

    return route_cost, route


# Input section
total_locations = int(input("Enter number of locations: "))
coords_list = []
print("Enter coordinates for location")
for idx in range(total_locations):
    x_val, y_val = map(int, input().split())
    coords_list.append((x_val, y_val))

depot_location = coords_list[0]
initial_temp = 100
cool_rate = 0.99

final_cost, final_route = perform_simulated_annealing(coords_list, depot_location, total_locations, initial_temp, cool_rate)

print("Path: ", end=" ")
path_len = len(final_route)
for idx in range(path_len):
    if idx != path_len - 1:
        print("", final_route[idx] + 1, end="->")
    else:
        print(final_route[idx] + 1)
print("Cost for this path is:", round(final_cost, 2))
