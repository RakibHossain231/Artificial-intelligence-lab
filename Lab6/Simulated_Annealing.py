import random;
import math;
def simulated_annealing(maze, start, end, max_iterations, initial_temperature, cooling_rate):
      def heuristics(pos): # Return heuristics value of pos node
            return abs(pos[0]- end[0])+ abs(pos[1]- end[1])
      
      def get_neighbors(pos): # return valid neighbors for pos node
            moves= [(0,1), (1,0), (0,-1), (-1,0)] # neighbors= right, down, left, up
            neighbors= [] # store valid neighbor in here
            for move in moves: 
                  neighbor = (pos[0]+move[0], pos[1]+move[1]) # find neighbor individually
                  if 0<= neighbor[0]<=4 and  0<=neighbor[1]<=4 and maze[neighbor[0]][neighbor[1]]!=1: # check neighbor are in the maze and last condition in check obstracle
                        neighbors.append(neighbor) # if valid then add into array
            return neighbors # return valid neighbors
      

      current= start
      path = [current]
      temperature= initial_temperature
      visited= {current} # we can check neighbor are visited or not


      for _ in range(max_iterations):

            if current== end:  # if current node is goal then return
                  return path, True;

            neighbors= get_neighbors(current)
            neighbor= random.choice(neighbors) # choose neighbor randomly from valid neighbors array
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