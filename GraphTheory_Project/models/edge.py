class Edge:

    from_state = None
    to_state = None
    label = None
    isAccept = None

    def __init__(self, from_state, to_state, label, isAccept):
        self.from_state = from_state
        self.to_state = to_state
        self.label = label
        self.isAccept = isAccept

