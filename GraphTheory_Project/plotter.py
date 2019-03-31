import matplotlib.pyplot as plt
import networkx as nx
from models import State, Nfa, Edge

def plot(thompsonsConstructor):
    """
        Create and display a NetworkX network chart using matplotlib
    """

    tc = thompsonsConstructor # constructor param named for clarity, reassign for brevity
    stateSet = set() # set of all states in the NFA
    edgeLabels = {}

    duplicateSet = set()

    # states with an in degree > 0 cannot be the initial state
    inDegreeSet = set()
    for s in stateSet:
        inDegreeSet.add(s.e1)
        inDegreeSet.add(s.e2)

    initialState = None
    for s in stateSet:
        if s not in inDegreeSet:
            initialState = s

    # find any states which have two edges between them
    for s in tc.edgeList:
        for t in tc.edgeList:
            if(s != t):
                if(s.from_state == t.to_state and s.to_state == t.from_state):
                    # double edge found
                    # join each state to a new state with empty string
                    newState1 = State()
                    newState1.e1 = ""
                    newState1.label = "E"

                    # for s
                    # add the new edges
                    tc.edgeList.append(Edge(s.from_state, newState1, s.from_state.label, False))
                    tc.edgeList.append(Edge(newState1, s.to_state, newState1.label, False))

                    newState2 = State()
                    newState2.e1 = ""
                    newState2.label = "E"
                    # for t
                    tc.edgeList.append(Edge(t.from_state, newState2, "E", False))
                    tc.edgeList.append(Edge(newState2, t.to_state, "E", False))

                    # remove the old edges, since they have been replaced
                    tc.edgeList.remove(s)
                    tc.edgeList.remove(t)

    # add the new states (if any) to the stateset
    for s in tc.edgeList:
        stateSet.add(s.from_state)
        stateSet.add(s.to_state)
        # also add the label
        edgeLabels[(s.from_state, s.to_state)] = s.label

    # states with an in degree > 0 cannot be the initial state
    inDegreeSet = set()
    for s in stateSet:
        inDegreeSet.add(s.e1)
        inDegreeSet.add(s.e2)

    initialState = None
    for s in stateSet:
        if s not in inDegreeSet:
            initialState = s


    # drawing the graph
    G = nx.DiGraph()
    G.add_nodes_from(stateSet) # add all states
    colorMap = []
    # set colour dependent on state
    for g in G:
        if g.e1 is None and g.e2 is None:
            colorMap.append('green')
        if g == initialState:
            colorMap.append('orange')
        else: colorMap.append('blue')

    # add all edges in edge list to the graph with a default colour
    for s in tc.edgeList:
        G.add_edge(s.from_state, s.to_state, node_color = 'blue')

    # set a layout
    pos = nx.fruchterman_reingold_layout(G)
    # draw the edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edgeLabels, node_color = colorMap)
    # draw the chart
    nx.draw(G, pos, node_color = colorMap)
    # show the matplotlib plot
    plt.show()

def getInitialState(stateSet):
    inDegreeSet = set()
    for s in stateSet:
        inDegreeSet.add(s.e1)
        inDegreeSet.add(s.e2)