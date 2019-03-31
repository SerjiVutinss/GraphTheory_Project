from utils import Stack
# Shunting Yard Algorithm

# Adapted from code by Ian McLoughlin -
# https://web.microsoftstream.com/video/cfc9f4a2-d34f-4cde-afba-063797493a90

class ShuntingYard:

    @staticmethod
    def shunt(infix):

        specials = {'*': 50, '.': 40, '|': 30}

        postfix = "" # output string
        #stack = "" # stack for unused characters?
        stack = Stack()

        # loop through infix string
        for c in infix:
            if c == '(':
                # found an open bracket, push to stack
                #stack = stack + c
                stack.push(c)
            elif c == ')':
                # loop until an open bracket is found on stack
                #while stack[-1] != '(':
                while stack.peek() != '(':
                    # concatenate the next character on the stack
                    # to the return string
                    #postfix = postfix + stack[-1]
                    postfix = postfix +  stack.pop()
                    # remove the character from the stack
                    #stack = stack[:-1]
                    #stack.pop()
                # remove the bracket from the stack
                #stack = stack[:-1]
                stack.pop()

            elif c in specials:

			    # NB
                #while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):

                while stack.isEmpty() != True and specials.get(c, 0) <= specials.get(stack.peek(), 0):
			    # get the special character from the dict
			    # concatenate the next character on the stack
			    # to the return string
                    postfix = postfix + stack.pop()
				    # remove the character from the stack
                    #stack = stack[:-1]
                    #stack.pop()
                #stack = stack + c
                stack.push(c)

            else:
                # just concatenate to string
                postfix = postfix + c
                # loop until stack is empty
        while stack.isEmpty() != True:
            # concatenate the next character on the stack
            # to the return string
            #postfix = postfix + stack[-1]
            postfix  = postfix + stack.pop()
            # remove the character from the stack
            #stack = stack[:-1]
            #stack.pop()

        print (infix, postfix)
        return postfix
