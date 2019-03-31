from models import Nfa, State, Edge
from utils import Stack

import plotter

# definition and precedence of special characters (operators)
regex_operators = {'|': 10, '.': 20, '+':25, '*': 30}

class ThompsonsConstructor():
    """
        Class which builds an NFA from the postfix string supplied to its constructor

        @param postfix - postfix notation string used to build the NFA

        @property solutionNfa - the resulting NFA built from the postfix string
        @property edgeList - a list of Edge objects, each representing an edge joining one state to another
        @property 
    """


    postfix = None # postfix string, constructor parameter
    nfaStack = None # stack data structure (utils.stack) used to build the NFA
    solutionNfa = None # final NFA representation of the postfix string
    
    # List of all connections between states - used to build charts
    # Note that while any NFA may not actually be charted by the application,
    # it is best to create the edge list while creating the NFA
    edgeList = None 

    stateCount = None

    def __init__(self, postfix):
        self.postfix = postfix
        self.edgeList = list()
        self.buildNfaFromPostFix()

    def addToEdgeList(self, from_state, to_state, label):
        """Helper method to add edge to the edge list - created function because it is called many times in the class"""
        self.edgeList.append(Edge(from_state, to_state, label, True))

    def buildNfaFromPostFix(self):
        """Build the solution NFA for this construction's postfix string"""
        self.stateCount = 0
        # keep track of all states in this set
        self.nfaSet = set()
        # create a stack for use within the algorithm,
        # the last element remaining on the stack once the algorithm
        # completes will be the 'solution' NFA
        self.nfaStack = Stack()

        # loop through the postfix string, dealing with any special
        # characters first
        for c in self.postfix:
            # if c is in the special characters...
            if(c in regex_operators):
                # handle special characters using helper methods
                if(c == '.'):
                    self.handleConcat()
                if(c == '|'):
                    self.handleOr()
                if(c == '*'):
                    self.handleStar()

            else:
                # create a new inital and accept state
                initial, accept = State(), State()

                ## TODO: perhaps remove this code
                #initial.stateNumber = self.stateCount
                #self.stateCount += 1
                ##accept = State()
                #accept.stateNumber = self.stateCount
                #self.stateCount += 1
                #####

                initial.label = c # label is the character read
                initial.e1 = accept # point first edge to the accept state

                # add the edge to the edge list
                self.addToEdgeList(initial, accept, c)

			    # create a new nfa using the two states and push to stack
                self.nfaStack.push(Nfa(initial, accept))
        self.solutionNfa = self.nfaStack.pop()

    def handleConcat(self):
        """Handles the AND (.) special character (operator)"""
        # It can be assumed that there are at least two NFAs
        # on the stack, else there would be no concat operator
        n2 = self.nfaStack.pop()
        n1 = self.nfaStack.pop()
        # join the accept of the first NFA to the initial of the second NFA
        n1.acceptState.e1 = n2.initialState
        # add this as an edge to the edgelist
        self.addToEdgeList(n1.acceptState, n2.initialState, "E")
        # create a new nfa using the two states and push to stack
        self.nfaStack.push(Nfa(n1.initialState, n2.acceptState))

    def handleOr(self):
        """Handles the OR (|) special character (operator)"""
		# It can be assumed that there are at least, two NFAs
        # on the stack, else there would be no OR operator
        n2 = self.nfaStack.pop()
        n1 = self.nfaStack.pop()
		# create new initial and accept states
        initial, accept = State(), State()
        # connect the new initial state to the initial states of the nfas
        initial.e1 = n1.initialState
        initial.e2 = n2.initialState
        # add the above edges to the edgelist
        self.addToEdgeList(initial, n1.initialState, "E")
        self.addToEdgeList(initial, n2.initialState, "E")
        # connect the accept state to the accept states of the nfas
        n1.acceptState.e1 = accept
        n2.acceptState.e1 = accept
        # add the above edges to the edgelist
        self.addToEdgeList(n1.acceptState, accept, "E")
        self.addToEdgeList(n2.acceptState, accept, "E")
        # create a new nfa using the two states and push to stack
        self.nfaStack.push(Nfa(initial, accept))

    def handleStar(self):
        """Handles the Kleene Star (zero or more) (*) special character (operator)"""
        # pop single NFA since this has the least order of
        # precedence...
        n1 = self.nfaStack.pop()
        # create new initial and accept states
        initial, accept = State(), State()
        # join the new initial state to the nfa initial state and the new
        # accept state
        initial.e1 = n1.initialState
        initial.e2 = accept
        # add the above edges to the edgelist
        self.addToEdgeList(initial, n1.initialState, "E")
        self.addToEdgeList(initial, accept, "E")
        # join old acept state to new accept state and nfa1's
        # initial state
        n1.acceptState.e1 = n1.initialState
        n1.acceptState.e2 = accept
        # add the above edges to the edgelist
        self.addToEdgeList(n1.acceptState, n1.initialState, "E")
        self.addToEdgeList(n1.acceptState, accept, "E")
        # create a new nfa using the two states and push to stack
        self.nfaStack.push(Nfa(initial, accept))

    def handleCross(self):
        """Handles the Kleene Plus (one or more) (*) special character (operator)"""
        # pop single NFA since this has the least order of
        # precedence...
        n1 = self.nfaStack.pop()
        # create new initial and accept states
        initial, accept = State(), State()
        # join the new initial state to the nfa initial state
        initial.e1 = n1.initialState
        # and add as an edge to the edgelist
        self.addToEdgeList(initial, n1.initialState, "E")
        # join old acept state to new accept state and nfa1's
        # initial state
        n1.acceptState.e1 = n1.initialState
        n1.acceptState.e2 = accept
        # add the above edges to the edge list
        self.addToEdgeList(n1.acceptState, n1.initialState, "E")
        self.addToEdgeList(n1.acceptState, accept, "E")
        # create a new nfa using the two states and push to stack
        self.nfaStack.push(Nfa(initial, accept))