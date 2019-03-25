#from samples_ian import sample_runner
from models import State, Nfa

from algorithms import ThompsonsConstructor, ShuntingYard

def main():
    print "Starting..."
    #sample_runner.run()
    n =  Nfa(State(), State())
    s = State()

    infix = "a*a"

    postfix = ShuntingYard.shunt(infix)
    print "POSTFIX: " + postfix

    t = ThompsonsConstructor(postfix)

    print t.solutionNfa

    print len(t.nfaSet)

    for n in t.nfaSet:
        print n.initialState.e1
        print n.initialState.e2
        print n.acceptState.e1
        print n.acceptState.e2

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

if __name__ == "__main__":
    main()
