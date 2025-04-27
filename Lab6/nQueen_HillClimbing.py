import random
def nQueen_hill_climbing(board, boardSize, max_iteration):
    
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
    
    
    # Hill climbing algorithm
    for x in range(max_iteration):
        current_h = get_heuristic(board)
        
        if current_h == 0: # If there are no conflicts, the solution is found.
            return True, board,x
            break 

        neighbors = get_neighbors(board)
        best_neighbor = min(neighbors, key=get_heuristic)
        best_h = get_heuristic(best_neighbor)

        if best_h >= current_h:
            break # Stuck, no good solution
        else:
            board = best_neighbor
    return None, board,x    



# ==== Main ====
board= [1,2,3,2]
random.shuffle(board)
n = 4 #int(input("Enter the Queen size: "))
# for x in range (n):
#     print("Enter Queen ", x+1, "position : ", end=" ")
#     x,y= map(int, input().split());
#     board.append(y)
    
maxIteration= 100 #int(input("Enter the max iteration: "))  
 
result, position, howTimesExecutes= nQueen_hill_climbing(board, n, maxIteration)

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
