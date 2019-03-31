class Result:

    string = None
    infix = None
    postfix = None
    isAccepted = None

    #string, infix, nfa.acceptState in currentStates, postfix

    def __init__(self, string, infix, isAccepted, postfix):
        self.string = string
        self.infix = infix
        self.isAccepted = isAccepted
        self.postfix = postfix

    def printResult(self):
        displayString = ''
        if(self.string == ''):
            displayString = "{Empty}"
        else:
            displayString = self.string
        print displayString + " in " + self.infix + " = " + str(self.isAccepted) + " (postfix = " + self.postfix + ")"

