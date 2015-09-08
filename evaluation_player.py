import heapq

from assignment2 import Player


class EvaluationPlayer(Player):
    def move(self, state):
        """Calculates the best move after 1-ply look-ahead with a simple evaluation function.

        Args:
            state (State): The current state of the board.

        Returns:
            the next move (Action)
        """

        # *You do not need to modify this method.*
        best_move = None
        max_value = -1.0
        my_color = state.to_play.color

        for action in state.actions():
            if self.is_time_up():
                break

            result_state = state.result(action)
            value = self.evaluate(result_state, my_color)
            if value > max_value:
                max_value = value
                best_move = action

        # Return the move with the highest evaluation value
        return best_move

    def evaluate(self, state, color):
        """Evaluates the state for the player with the given stone color.

        This function calculates the length of the longest ``streak'' on the board
        (of the given stone color) divided by K.  Since the longest streak you can
        achieve is K, the value returned will be in range [1 / state.K, 1.0].

        Args:
            state (State): The state instance for the current board.
            color (int): The color of the stone for which to calculate the streaks.

        Returns:
            the evaluation value (float), from 1.0 / state.K (worst) to 1.0 (win).
        """

        # TODO implement this
        
	#Grabs the width and height of the board
	width = state.M
	height = state.N

	#Initializes max streak
	maxv = 0

	#Uses flag for initial check of length
	flag = 1
	
	#Checks all possible piece on board to count the streak
	for x in range(width):
	    for y in range(height):
	    	
		#Checks if there is even a piece with the color on there
	    	if (state.board[x][y] == color) and (flag == 1):
		    flag = 0
		    maxv = 1

		#Initialize temp max streak directional values at each point
	        tmp = 0
	        tmp2 = 0
		tmp3 = 0
		tmp4 = 0

		#Checks if there is a potential streak in a given direction.
		#If there is, then it'll call the traverse method which will
		#continue checking in that direction until no more colors match.
		#Returns the longest streak it can find in that direction.
		if (x+1 != width) and (color == state.board[x][y]) and (color == state.board[x+1][y]):
		    tmp = self.traverse(state, 1, x, y, color)
		if (y+1 != height) and (color == state.board[x][y]) and (color == state.board[x][y]):
		    tmp2 = self.traverse(state, 2, x, y, color)
		if (x+1 != width) and (y+1 != height) and (color == state.board[x][y]) and (color == state.board[x+1][y+1]):
		    tmp3 = self.traverse(state, 3, x, y, color)
		if (x+1 != width) and (y-1 != -1) and (color == state.board[x][y]) and (color == state.board[x+1][y-1]):
		    tmp4 = self.traverse(state, 4, x, y, color)
		
		#Compares for the greatest values
		tmp5 = max(tmp,tmp2,tmp3, tmp4)
		
		#Checks if it is greater than current value then updates
		if tmp5 > maxv:
			maxv = tmp5

	#Reurns the streak/K as a float.
	return (float(maxv)/float(state.K))

    #Method that checks for streak length in one of four directions.
    #Returns the length of the streak when completed.
    def traverse(self, state, direction, x, y, color):
    	width = state.M
	height = state.N

	count = 0
	if direction == 1:
	    flag = 1
	    while flag == 1:
	        if (x+1 != width) and (state.board[x+1][y] == color):
		    x = x + 1
		    count = count + 1
		else:
		    flag = 0
	elif direction == 2:
	    flag = 1
	    while flag == 1:
	        if (y+1 != height) and (state.board[x][y+1] == color):
		    y = y + 1
		    count = count + 1
		else:
		    flag = 0
	elif direction == 3:
	    flag = 1
	    while flag == 1:
	        if (x+1 != width) and (y+1 != height) and (state.board[x+1][y+1] == color):
		    x = x + 1
		    y = y + 1
		    count = count + 1
		else:
		    flag = 0
	elif direction == 4:
	    flag = 1
	    while flag == 1:
	        if (x+1 != width) and (y-1 != -1) and (state.board[x+1][y-1] == color):
		    x = x + 1
		    y = y - 1
		    count = count + 1
		else:
		    flag = 0


        return count + 1
