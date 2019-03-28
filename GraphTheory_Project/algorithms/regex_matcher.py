from models import State, Nfa
from algorithms import ThompsonsConstructor, ShuntingYard

def match(infix, string):
    """Match string to infix reg ex"""
    postfix = ShuntingYard.shunt(infix)
    # shunt and compile the reg ex
    tc = ThompsonsConstructor(postfix)
    nfa = tc.solutionNfa

    for s in tc.edgeList:
        print hash(s.from_state), s.label, hash(s.to_state)

	# set of current and next states
    currentStates = set()
    nextStates = set()
	# add initial state of nfa to current states
    currentStates |= followEedges(nfa.initialState)

	# loop through each character in the string
    for s in string:
		# loop through current states
        for c in currentStates:
            # check if state is labelled s
            if(c.label == s):
				# follow its E edge (will only be one)
                nextStates |= followEedges(c.e1)
		# set current to next and clear next set
        currentStates = nextStates
        nextStates = set()
	    # return state is in set of current
	    # return state is in set of current

    return (nfa.acceptState in currentStates)


def followEedges(state):
	"""Returns the set of states that can be reached from
		the state, following the arrows"""

	# create a new set with state as its only member
	states = set()
	states.add(state)
	# if state has e arrows
	if(state.label is None):
		# check if edge one is a state
		if(state.e1 is not None):
			# recursively follow the edges
			# union states
			states |= followEedges(state.e1)
		# check if edge one is a state
		if(state.e2 is not None):
			# recursively follow the edges
			# union states
			states |= followEedges(state.e2)

	# return the set of states
	return states
