import thompsons_constructor
import shunting_yard

def run():

    print(thompsons_constructor.compile("ab.cd.|"))
    print(thompsons_constructor.compile("aa.*"))

    print(shunting_yard.shunt("(a.b)|(c*.d)"))
    print(shunting_yard.shunt("(a|b).(c*.d)"))

    infixes = ["a.b.c", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
    strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

    for i in infixes:
        for s in strings:
            print match(i, s), i, s


def followEedges(state):
	"""Returns the set of states that can be reached from
		the state, following the arrows"""

	# create a new set with state as its only member
	states = set()
	states.add(state)
	# if state has e arrows
	if(state.label is None):
		# check if edge one is a state
		if(state.edge1 is not None):
			# recursively follow the edges
			# union states
			states |= followEedges(state.edge1)
		# check if edge one is a state
		if(state.edge2 is not None):
			# recursively follow the edges
			# union states
			states |= followEedges(state.edge2)

	# return the set of states
	return states

def match(infix, string):
	"""Match string to infix reg ex"""

	# shunt and compile the reg ex
	postfix = shunting_yard.shunt(infix)
	nfa = thompsons_constructor.compile(postfix)

	# set of current and next states
	currentStates = set()
	nextStates = set()

	# add initial state of nfa to current states
	currentStates |= followEedges(nfa.initial)

	# loop through each character in the string
	for s in string:
		# loop through current states
		for c in currentStates:
			# check if state is labelled s
			if(c.label == s):
				# follow its E edge (will only be one)
				nextStates |= followEedges(c.edge1)
		# set current to next and clear next set
		currentStates = nextStates
		nextStates = set()
	# return state is in set of current states
	return (nfa.accept in currentStates)
