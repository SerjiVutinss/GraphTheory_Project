class Edge:

    from_state = None
    to_state = None
    label = None

    def __init__(self, from_state, to_state, label):
        self.from_state = from_state
        self.to_state = to_state
        self.label = label

