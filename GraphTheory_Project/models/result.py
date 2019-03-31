class Result:
    """
        Class which represents a Result of comparing a string against a reg-ex
    """
    string = None
    infix = None
    postfix = None
    isAccepted = None
    thompsonsConstruction = None

    #string, infix, nfa.acceptState in currentStates, postfix

    def __init__(self, string, infix, isAccepted, postfix, thompsonsConstruction):
        self.string = string
        self.infix = infix
        self.isAccepted = isAccepted
        self.postfix = postfix
        self.thompsonsConstruction = thompsonsConstruction

    def printResult(self):
        displayString = ''
        if(self.string == '' or self.string == None):
            displayString = "{Empty}"
        else:
            displayString = self.string
        print displayString + " in " + self.infix + " = " + str(self.isAccepted) + " (postfix = " + self.postfix + ")"

