class State:

    label = None
    # edges - used to connect to other states
    e1 = None
    e2 = None
    isFirst = None
    stateNumber = None

    def __hash__(self):
        return id(self) + id(self.e1) + id(self.e2) + id(self.stateNumber)

    def __str__(self):
        if(self.stateNumber != None):
            if(self.stateNumber == 0):
                return 'I'
            else:
                #return str(self.stateNumber)
                return ""
        else:
            return "A"

    def followEdges(state):
        """Returns the set of states that can be reached from the state, following the arrows"""
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

