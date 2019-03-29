class Edge:

    from_state = None
    to_state = None
    label = None
    isAccept = None

    def __hash__(self):
        return id((hash(self.from_state) * 2) + (hash(self.to_state) * 3))

    def __init__(self, from_state, to_state, label, isAccept):
        self.from_state = from_state
        self.to_state = to_state
        self.label = label
        self.isAccept = isAccept

