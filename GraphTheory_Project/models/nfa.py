class Nfa:

    initialState = None
    acceptState = None

    def __init__(self, initial, accept):
        self.initialState = initial
        self.acceptState = accept