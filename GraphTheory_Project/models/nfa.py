class Nfa:
    """
        An NFA which is built using Thompson's Construction
    """
    initialState = None
    acceptState = None

    def __init__(self, initial, accept):
        self.initialState = initial
        self.acceptState = accept