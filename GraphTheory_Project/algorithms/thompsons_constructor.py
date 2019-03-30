from models import Nfa, State, Edge
import plotter

regex_operators = {'|': 10, '.': 20, '+':25, '*': 30}

class ThompsonsConstructor():

    postfix = None
    #nfaSet = None
    nfaStack = None

    solutionNfa = None

    edgeList = None

    stateCount = None

    def __init__(self, postfix):
        self.postfix = postfix
        self.edgeList = list()
        self.buildNfaFromPostFix()
        #self.buildEdgeSet()

    def addToEdgeList(self, from_state, to_state, label):
        self.edgeList.append(Edge(from_state, to_state, label, True))

    def buildNfaFromPostFix(self):
        """Takes a postfix reg ex pattern as a parameter and returns the NFA"""
        self.stateCount = 0
        # keep track of all states in this set
        self.nfaSet = set()
        # create a stack for use within the algorithm,
        # the last element remaining on the stack once the algorithm
        # completes will be the 'solution' NFA
        self.nfaStack = []

        # loop through the postfix string, dealing with any special
        # characters first
        for c in self.postfix:
            # if c is in the special characters...
            if(c in regex_operators):
                # handle special characters
                if(c == '.'):
                    self.handleConcat()
                if(c == '|'):
                    self.handleOr()
                if(c == '*'):
                    self.handleStar()

            else:
                initial = State()
                initial.stateNumber = self.stateCount
                self.stateCount += 1
                accept = State()
                accept.stateNumber = self.stateCount
                self.stateCount += 1
                initial.label = c # label is char
                initial.e1 = accept # point to the accept state

                self.addToEdgeList(initial, accept, c)

                newNfa = Nfa(initial, accept)
                #self.nfaSet.add(newNfa)
			    # create a new nfa using the two states and push to stack
                self.nfaStack.append(newNfa)


        self.solutionNfa = self.nfaStack.pop()

    def handleConcat(self):
        # It can be assumed that there are at least, two NFAs
        # on the stack, else there would be no concat operator
        n2 = self.nfaStack.pop()
        n1 = self.nfaStack.pop()

        # join the accept of the first NFA to the initial
        # of the second and create a new NFA
        n1.acceptState.e1 = n2.initialState
        self.addToEdgeList(n1.acceptState, n2.initialState, "E")

        newNfa = Nfa(n1.initialState, n2.acceptState)
        # push this new NFA to the stack
        self.nfaStack.append(newNfa)
        #self.nfaSet.add(newNfa)

    def handleOr(self):
		# It can be assumed that there are at least, two NFAs
        # on the stack, else there would be no OR operator
        n2 = self.nfaStack.pop()
        n1 = self.nfaStack.pop()
		# create new initial and accept states
        initial = State()
        initial.stateNumber = self.stateCount
        self.stateCount += 1
        accept = State()
        initial.stateNumber = self.stateCount
        self.stateCount += 1
        # connect the initial state to the initial states of the nfas
        initial.e1 = n1.initialState
        initial.e2 = n2.initialState

        self.addToEdgeList(initial, n1.initialState, "E")
        self.addToEdgeList(initial, n2.initialState, "E")

        # connect the accept state to the accept states of the nfas
        n1.acceptState.e1 = accept
        n2.acceptState.e1 = accept

        self.addToEdgeList(n1.acceptState, accept, "E")
        self.addToEdgeList(n2.acceptState, accept, "E")

        # push a new nfa to the stack, using accept and initial states
        newNfa = Nfa(initial, accept)
        #self.nfaSet.add(newNfa)
        self.nfaStack.append(newNfa)

    def handleStar(self):
        # pop single NFA since this has the least order of
        # precedence...
        n1 = self.nfaStack.pop()
        # create new initial and accept states
        initial = State()
        initial.stateNumber = self.stateCount
        self.stateCount += 1
        accept = State()
        initial.stateNumber = self.stateCount
        self.stateCount += 1
        # join the new initial state to the nfa initial state
        # and the new accept state
        initial.e1 = n1.initialState
        initial.e2 = accept

        self.addToEdgeList(initial, n1.initialState, "E")
        self.addToEdgeList(initial, accept, "E")

        # join old acept state to new accept state and nfa1's
        # initial state
        n1.acceptState.e1 = n1.initialState
        n1.acceptState.e2 = accept

        self.addToEdgeList(n1.acceptState, n1.initialState, "E")
        self.addToEdgeList(n1.acceptState, accept, "E")
        
        # push new nfa to stack
        newNfa = Nfa(initial, accept)
        #self.nfaSet.add(newNfa)
        self.nfaStack.append(newNfa)

    def handleCross(self):
        # pop single NFA since this has the least order of
        # precedence...
        n1 = self.nfaStack.pop()
        # create new initial and accept states
        initial = State()
        initial.stateNumber = self.stateCount
        self.stateCount += 1
        accept = State()
        initial.stateNumber = self.stateCount
        self.stateCount += 1
        # join the new initial state to the nfa initial state
        initial.e1 = n1.initialState

        self.addToEdgeList(initial, n1.initialState, "E")

        # join old acept state to new accept state and nfa1's
        # initial state
        n1.acceptState.e1 = n1.initialState
        n1.acceptState.e2 = accept

        self.addToEdgeList(n1.acceptState, n1.initialState, "E")
        self.addToEdgeList(n1.acceptState, accept, "E")
        
        # push new nfa to stack
        newNfa = Nfa(initial, accept)
        #self.nfaSet.add(newNfa)
        self.nfaStack.append(newNfa)

    def buildEdgeSet(self):
        nfa = self.solutionNfa
        edgeSet = set()

        edgeSet |= self.followEedges(nfa.initialState)
        print len(edgeSet)


        return


    def followEedges(self, state):
        """Returns the set of states that can be reached from
		    the state, following the arrows"""

	    # create a new set with state as its only member
        edges = set()
        # check if edge one is a state
        if(state.e1 is not None):
            # recursively follow the edges
            # union states
            edges.add(Edge(state, state.e1))
            edges |= self.followEedges(state.e1)
	    # check if edge one is a state
        if(state.e2 is not None):
		    # recursively follow the edges
			# union states
            edges.add(Edge(state, state.e2))
            edges |= self.followEedges(state.e2)
	    # return the set of states
        return edges