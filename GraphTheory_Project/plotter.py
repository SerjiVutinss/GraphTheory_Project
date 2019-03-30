from models import State, Nfa, Edge

import matplotlib.pyplot as plt
import networkx as nx

def plot(thompsonsConstructor):
    G = nx.DiGraph()

    tc = thompsonsConstructor

    stateSet = set()
    edgeLabels = {}

    duplicateSet = set()


    for s in tc.edgeList:
        for t in tc.edgeList:
            if(s != t):
                if(s.from_state == t.to_state and s.to_state == t.from_state):
                    nS = State()

                    a = s.from_state
                    c = s.to_state

                    newState1 = State()
                    newState1.e1 = ""
                    newState1.label = "E"

                    # for s
                    tc.edgeList.append(Edge(s.from_state, newState1, s.from_state.label, False))
                    tc.edgeList.append(Edge(newState1, s.to_state, newState1.label, False))

                    newState2 = State()
                    newState2.e1 = ""
                    newState2.label = "E"
                    # for t
                    tc.edgeList.append(Edge(t.from_state, newState2, t.from_state.label, False))
                    tc.edgeList.append(Edge(newState2, t.to_state, newState2.label, False))

                    tc.edgeList.remove(s)
                    tc.edgeList.remove(t)

                    tc.edgeList.sort()

    for s in tc.edgeList:
        stateSet.add(s.from_state)
        stateSet.add(s.to_state)
        edgeLabels[(s.from_state, s.to_state)] = s.label
        #G.add_edge(s.from_state, s.to_state, node_color = 'blue')

    # states with an in degree > 0
    inDegreeSet = set()
    for s in stateSet:
        inDegreeSet.add(s.e1)
        inDegreeSet.add(s.e2)

    for s in stateSet:
        if s not in inDegreeSet:
            s.stateNumber = -1


    G.add_nodes_from(stateSet)
    colorMap = []
    for g in G:
        if g.e1 is None and g.e2 is None:
            colorMap.append('green')
        if g.stateNumber == -1:
            colorMap.append('orange')
        else: colorMap.append('blue')

    for s in tc.edgeList:
        G.add_edge(s.from_state, s.to_state, node_color = 'blue')

    pos = nx.fruchterman_reingold_layout(G, 2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edgeLabels, node_color = colorMap)
    nx.draw(G, pos, node_color = colorMap, with_labels = True)
    #nx.draw(G, pos, node_color = colorMap)

    plt.style.use(['dark_background'])

    #plt.axis('off')
    plt.axes().patch.set_facecolor('black')
    plt.show()
