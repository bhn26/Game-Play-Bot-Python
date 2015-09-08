from assignment2 import Player, State, Action
from sys import maxint

trans = {}

class AlphaBetaPlayer(Player):
    def move(self, state):
        """Calculates the best move from the given board using the minimax algorithm with alpha-beta pruning.

        Args:
            state (State): The current state of the board.

        Returns:
            the next move (Action)
        """

        # TODO implement this
        return ALPHABETASEARCH(self, state)

#MINIMAX search with alpha-beta pruning. Also implements a transposition
#table. Calls MINVALUE with an initially empty transposition table.
def ALPHABETASEARCH(self, state):
	v = -maxint
	argmax = 0
	for action in state.actions():
		minv = MINVALUE(self, state.result(action), -maxint, maxint)
		if v < minv:
			v = minv
			argmax = action
	return argmax

#MAXVALUE returns a utilite value based on MIN's best move. It also checks
#to see if there is already a beta value that can be checked to prune. It
#then checks to see if the max between alpha and current v to update value.
#It stores the moved state into a transposition table and then passes it on
#into MINVALUE to make sure it doesn't check twice.
def MAXVALUE(self, state, alpha, beta):
	if state.is_terminal():
		return state.utility(self)
	
	v = -maxint
	for a in state.actions():
		move = state.result(a)
		h = hash(move)
		if h in trans:
			v = trans[h]
		else:
			v = max(v, MINVALUE(self, move, alpha, beta))
			trans[h] = v
		if v >= beta:
			return v
		alpha = max(alpha, v)
	return v

#Exactly the same as MAXVALUE except instead of checking beta, we check alpha.
#Our goal is to take the action with MIN value based on MAX's best move while
#pruning unecessary checks.
def MINVALUE(self, state, alpha, beta):
	if state.is_terminal():
		return state.utility(self)
	
	v = maxint
	for a in state.actions():
		move = state.result(a)
		h = hash(move)
		if h in trans:
			v = trans[h]
		else:
			v = min(v, MAXVALUE(self, move, alpha, beta))
			trans[h] = v
		if v <= alpha:
			return v
		beta = min(beta, v)
	return v
