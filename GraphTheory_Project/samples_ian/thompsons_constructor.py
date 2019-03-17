# Thompson's Algorithm

# Written by Ian McLoughlin https://web.microsoftstream.com/video/5e2a482a-b1c9-48a3-b183-19eb8362abc9

# use None for a label representing 'E' arrows
class state:
	label = None
	edge1 = None
	edge2 = None


class nfa:
	initial = None
	accept = None

	def __init__(self, initial, accept):
		self.initial = initial
		self.accept = accept

def compile(postfix):
	nfaStack = []

	for c in postfix:
		if(c == '.'):
			nfa2 = nfaStack.pop()
			nfa1 = nfaStack.pop()

			# join the two nfas together
			nfa1.accept.edge1 = nfa2.initial
			nfaStack.append(nfa(nfa1.initial, nfa2.accept))

		elif(c == '|'):
			# pop two nfas from the stack
			nfa2 = nfaStack.pop()
			nfa1 = nfaStack.pop()
			# create new initial and accept states
			initial = state()
			accept = state()
			# connect the initial state to the initial states of the nfas
			initial.edge1 = nfa1.initial
			initial.edge2 = nfa2.initial
			# connect the accept state to the accept states of the nfas
			nfa1.accept.edge1 = accept
			nfa2.accept.edge1 = accept
			# push a new nfa to the stack, using accept and initial states
			nfaStack.append(nfa(initial, accept))

		elif (c == '*'):
			# pop single nfa
			nfa1 = nfaStack.pop()
			# create new initial and accept states
			initial = state()
			accept = state()
			# join the new initial state to the nfa initial state
			# and the new accept state
			initial.edge1 = nfa1.initial
			initial.edge2 = accept
			# join old acept state to new accept state and nfa1's
			# initial state
			nfa1.accept.edge1 = nfa1.initial
			nfa1.accept.edge2 = accept
			# push new nfa to stack
			nfaStack.append(nfa(initial, accept))
		else:
			initial = state()
			accept = state()

			initial.label = c # label is char
			initial.edge1 = accept # point to the accept state

			# create a new nfa using the two states and push to stack
			nfaStack.append(nfa(initial, accept))

	# only should be one nfa on stack at this point
	return nfaStack.pop()
