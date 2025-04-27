import random;
import math;
def simulated_annealing(maze, start, end, max_iterations, initial_temperature, cooling_rate):
      def heuristics(pos):
            return abs(pos[0]- end[0])+ abs(pos[1]- end[1])
      def get_neighbors(pos):
            moves= [(0,1), (1,0), (0,-1), (-1,0)]
            neighbors= []
            for move in moves:
                  neighbor = (pos[0]+move[0], pos[1]+move[1])
                  if 0<= neighbor[0]<=4 and  0<=neighbor[1]<=4 and maze[neighbor[0]][neighbor[1]]!=1:
                        neighbors.append(neighbor)
            return neighbors
      current= start
      path = [current]
      temperature= initial_temperature
      visited= {current}


      while True:

            if current== end:
                  return path, True;
            if temperature<=10:
                  print("Cooled Temperature")
                  break
            
            neighbors= get_neighbors(current)
            neighbor= random.choice(neighbors)
            delta= heuristics(neighbor) - heuristics(current)

            if delta<0 and neighbor not in visited:
                  current= neighbor
                  path.append(current)
                  visited.add(current)
                  

            else:
                  probability= math.exp(-delta/temperature)
                  random_number= random.uniform(0,1)
                  if random_number<=probability:
                        current= neighbor
                        neighbors.append(current)
                        visited.add(current)
            temperature *= cooling_rate
      return path, False;      

      


maze= [
      [0,1,0,0,0],
      [0,1,0,1,0],
      [0,0,0,1,0],
      [0,1,0,1,0],
      [1,1,0,1,0]
      ]  


start= (0,0)
end = (4,4)
max_iterations= 100
initial_temperature= 100
cooling_rate= 0.95
path, result= simulated_annealing(maze, start, end, max_iterations, initial_temperature, cooling_rate)
print(result, path)