# Shunting Yard Algorithm

# Written by Ian McLoughlin - https://web.microsoftstream.com/video/cfc9f4a2-d34f-4cde-afba-063797493a90
def shunt(infix):
	
	specials = {'*': 50, '.': 40, '|': 30}

	postfix = "" # output string
	stack = "" # stack for unused characters?

	# loop through infix string
	for c in infix:
		if c == '(':
			# found an open bracket, push to stack
			stack = stack + c
		elif c == ')':
			# loop until an open bracket is found on stack
			while stack[-1] != '(':
				# concatenate the next character on the stack
				# to the return string
				postfix = postfix + stack[-1]
				# remove the character from the stack
				stack = stack[:-1]
			# remove the bracket from the stack
			stack = stack[:-1]

		elif c in specials:

			# NB 
			while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
			# get the special character from the dict
			# concatenate the next character on the stack
			# to the return string
				postfix = postfix + stack[-1]
				# remove the character from the stack
				stack = stack[:-1]
			stack = stack + c

		else:
			# just concatenate to string
			postfix = postfix + c
			# loop until stack is empty
	while stack:
		# concatenate the next character on the stack
		# to the return string
		postfix = postfix + stack[-1]
		# remove the character from the stack
		stack = stack[:-1]

	return postfix
