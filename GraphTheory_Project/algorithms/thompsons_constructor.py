from models import Nfa, State

regex_operators = {'|': 10, '.': 20, '*': 30}

class ThompsonsConstructor():

    postfix = None
    nfaSet = None
    nfaStack = None

    #stateSet = None

    solutionNfa = None

    def __init__(self, postfix):
        self.postfix = postfix
        self.buildNfaFromPostFix()
        #self.followEedges()

    def buildNfaFromPostFix(self):
        """Takes a postfix reg ex pattern as a parameter and returns the NFA"""

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
                accept = State()
                initial.label = c # label is char
                initial.e1 = accept # point to the accept state
                newNfa = Nfa(initial, accept)
                self.nfaSet.add(newNfa)
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


        newNfa = Nfa(n1.initialState, n2.acceptState)
        # push this new NFA to the stack
        self.nfaStack.append(newNfa)
        self.nfaSet.add(newNfa)

    def handleOr(self):
		# It can be assumed that there are at least, two NFAs
        # on the stack, else there would be no OR operator
        n2 = self.nfaStack.pop()
        n1 = self.nfaStack.pop()
		# create new initial and accept states
        initial = State()
        accept = State()
        # connect the initial state to the initial states of the nfas
        initial.e1 = n1.initialState
        initial.e2 = n2.initialState
        # connect the accept state to the accept states of the nfas
        n1.acceptState.e1 = accept
        n2.acceptState.e1 = accept
        # push a new nfa to the stack, using accept and initial states
        newNfa = Nfa(initial, accept)
        self.nfaSet.add(newNfa)   
        self.nfaStack.append(newNfa)

    def handleStar(self):
        # pop single NFA since this has the least order of
        # precedence...
        n1 = self.nfaStack.pop()
        # create new initial and accept states
        initial = State()
        accept = State()
        # join the new initial state to the nfa initial state
        # and the new accept state
        initial.e1 = n1.initialState
        initial.e2 = accept
        # join old acept state to new accept state and nfa1's
        # initial state
        n1.acceptState.e1 = n1.initialState
        n1.acceptState.e2 = accept
        # push new nfa to stack
        newNfa = Nfa(initial, accept)
        self.nfaSet.add(newNfa)			    
        self.nfaStack.append(newNfa)

    def followEedges(self):
        """Returns the set of states that can be reached from
		the state, following the arrows"""

        # create a new set with state as its only member
        self.stateSet = {}
        #print len(self.nfaSet)
        for n in self.nfaSet:
            self.followEdge(n.initialState)
            self.followEdge(n.acceptState)

        #print len(self.stateSet)
        #for n in self.stateSet:
        #    print n.label

    def followEdge(self, state):
        """Follw edges recursively"""
        if(state.e1 != None):
            self.stateSet[state] = state.e1
            self.followEdge(state.e1)
        if(state.e2 != None):
            self.stateSet[state] = state.e2
            self.followEdge(state.e2)
        if(state.e1 != None):
            self.stateSet[state] = state.e1
            self.followEdge(state.e1)
        if(state.e2 != None):
            self.stateSet[state] = state.e2
            self.followEdge(state.e2)
