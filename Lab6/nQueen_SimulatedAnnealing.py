import math
import random
def nQueen_hill_climbing(board, boardSize, temperature, coolingRate):
    
    def get_heuristic(board): # How many queens are attacking how many queens?
        h = 0
        for i in range(boardSize):
            for j in range(i + 1, boardSize): 
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j): # If it is in the same row or diagonally
                    h += 1
        return h

    def get_neighbors(board): # Creates all possible positions by moving a queen
        neighbors = []
        for col in range(boardSize):
            for row in range(boardSize):
                if board[col] != row:
                    new_board = board.copy()
                    new_board[col] = row
                    neighbors.append(new_board)
        return neighbors
    temp= temperature
    count=0
    # Hill climbing algorithm
    while True:
        count+=1
        current_h = get_heuristic(board)
        if current_h == 0: # If there are no conflicts, the solution is found.
            return True, board,count
        if temp<=10:
            return None, board, count
    
        neighbors = get_neighbors(board)
        best_neighbor = min(neighbors, key=get_heuristic)
        best_h = get_heuristic(best_neighbor)
        
        delta= best_h- current_h

        if delta <0:
            board= best_neighbor
        else:
            probability= math.exp(-delta/temp)
            random_Number= random.uniform(0,1)
            if random_Number<=probability:
                board = best_neighbor
        temp*=coolingRate   

# ==== Main ====
board= [3,2,3,3]
random.shuffle(board)
n = 4 #int(input("Enter the Queen size: "))
# for x in range (n):
#     print("Enter Queen ", x+1, "position : ", end=" ")
#     x,y= map(int, input().split());
#     board.append(y)
    
initialTemperature= 100 #int(input("Enter the Initial Temperature: "))
coolingRate= 0.98 #int(input("Enter the cooling rate: "))
 
 
result, position, howTimesExecutes= nQueen_hill_climbing(board, n, initialTemperature, coolingRate)

#Output Print
print("Reach the goal: ", result, ", and Try time ", howTimesExecutes)
print("Board")
for x in range (n):
    for y in range(n):
        if y==position[x]:
            print("", 1, end=" ")
        else:
            print("", 0, end=" ")
    print()    
