from assignment2 import Player, State, Action
from sys import maxint
import datetime

class MinimaxPlayer(Player):
    def move(self, state):
        """Calculates the best move from the given board using the minimax algorithm.

        Args:
            state (State): The current state of the board.

        Returns:
            the next move (Action)
        """
		
        return MINIMAXDECISION(self, state)

#Takes the action with MAX value based on MIN's best move.
#It checks all states and the best move MINVALUE and give and keeps track
#of which is the current largest value.
#Reference: Class slides
def MINIMAXDECISION(self, state):
	aa = datetime.datetime.now()
	v = -maxint
	argmax = 0
	for a in state.actions():
		minv = MINVALUE(self, state.result(a))
		if v < minv:
			v = minv
			argmax = a
	b = datetime.datetime.now()
	print (b - aa)
	return argmax

#Does the same as MINIMAXDECISION excepts check for a terminal state in
#order to see if game is complete or not. Takes the action with the MAX
#value based on MIN's best move.
def MAXVALUE(self, state):
	if state.is_terminal():
		return state.utility(self)
	
	v = -maxint
	for a in state.actions():
		minv = MINVALUE(self, state.result(a))
		v = max(v, minv)
	return v

#Does the opposite of MAXVALUE. It takes the action with the MIN value based
#on MAX's best move. Also checks for terminal state.
def MINVALUE(self, state):
	if state.is_terminal():
		return state.utility(self)
	
	v = maxint
	for a in state.actions():
		maxv = MAXVALUE(self, state.result(a))
		v = min(v, maxv)
	return v
