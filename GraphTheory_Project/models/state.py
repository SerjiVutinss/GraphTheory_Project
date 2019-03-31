class State:
    """Represents a state within an NFA"""
    label = None
    # edges - used to connect to other states
    e1 = None
    e2 = None

    def __hash__(self):
        return id(self) + id(self.e1) + id(self.e2)

