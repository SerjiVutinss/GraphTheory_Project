from models import Nfa, State

regex_operators = {'|': 10, '.': 20, '*': 30}

class ThompsonsConstructor():

    postfix = None
    allStates = None
    nfaStack = None

    def __init__(self, postfix):
        self.postfix = postfix
        self.buildNfaFromPostFix()

    def buildNfaFromPostFix(self):
        """Takes a postfix reg ex pattern as a parameter and returns the NFA"""

        # keep track of all states in this set
        self.allStates = set()
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
                initial.edge1 = accept # point to the accept state

			    # create a new nfa using the two states and push to stack
                self.nfaStack.append(Nfa(initial, accept))

        return self.nfaStack.pop()

    def handleConcat(self):
        # It can be assumed that there are at least, two NFAs
        # on the stack, else there would be no concat operator
        n1 = self.nfaStack.pop()
        n2 = self.nfaStack.pop()

        # join the accept of the first NFA to the initial
        # of the second and create a new NFA
        n1.acceptState.e1 = n2.initialState
        newNfa = Nfa(n1.initial, n2.accept)
        # push this new NFA to the stack
        self.nfaStack.append(newNfa)

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
        self.nfaStack.append(Nfa(initial, accept))

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
        self.nfaStack.append(Nfa(initial, accept))




