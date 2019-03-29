from models import State, Nfa, Edge
from algorithms import ThompsonsConstructor, ShuntingYard

import matplotlib.pyplot as plt
import networkx as nx

def match(infix, string):
    """Match string to infix reg ex"""
    postfix = ShuntingYard.shunt(infix)
    # shunt and compile the reg ex
    tc = ThompsonsConstructor(postfix)
    nfa = tc.solutionNfa

    G = nx.DiGraph()

    stateSet = set()
    edgeLabels = {}

    duplicateSet = set()


    for s in tc.edgeList:
        for t in tc.edgeList:
            if(s != t):
                if(s.from_state == t.to_state and s.to_state == t.from_state):
                    print "Hello"

    for s in tc.edgeList:
        stateSet.add(s.from_state)
        stateSet.add(s.to_state)
        edgeLabels[(s.from_state, s.to_state)] = s.label
        #G.add_edge(s.from_state, s.to_state, node_color = 'blue')

    # states with an in degree > 0
    inDegreeSet = set()
    for s in stateSet:
        inDegreeSet.add(s.e1)
        inDegreeSet.add(s.e2)

    for s in stateSet:
        if s not in inDegreeSet:
            s.stateNumber = -1


    G.add_nodes_from(stateSet)
    colorMap = []
    for g in G:
        if g.e1 is None and g.e2 is None:
            colorMap.append('green')
        if g.stateNumber == -1:
            colorMap.append('orange')
        else: colorMap.append('blue')

    for s in tc.edgeList:
        G.add_edge(s.from_state, s.to_state, node_color = 'blue')

    pos = nx.fruchterman_reingold_layout(G)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edgeLabels, node_color = colorMap)
    nx.draw(G, pos, node_color = colorMap, with_labels = True)
    #nx.draw(G, pos, node_color = colorMap)

    plt.style.use(['dark_background'])

    #plt.axis('off')
    plt.axes().patch.set_facecolor('black')
    plt.show()

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
