from utils import Stack
# Shunting Yard Algorithm

# Adapted from code by Ian McLoughlin -
# https://web.microsoftstream.com/video/cfc9f4a2-d34f-4cde-afba-063797493a90
class ShuntingYard:

    @staticmethod
    def shunt(infix):
        """
            Function to convert an infix string into a postfix string
            @param infix - the infix string which will be converted to postfix
            @returns postfix - the postfix string generated from the infix paramater
        """
        specials = {'*': 50, '.': 40, '|': 30}

        postfix = "" # output string
        stack = Stack() # main data structure used in the algorithm

        # loop through infix string
        for c in infix:
            if c == '(':
                # found an open bracket, push to stack
                stack.push(c)
            elif c == ')': # note that this character never gets pushed to stack
                # loop until an open bracket is found on stack
                while stack.peek() != '(':
                    # pop next character from stack and append to postfix
                    postfix = postfix + stack.pop()
                # opening bracket was found on stack, remove and discard
                stack.pop()

            elif c in specials:
                # while the stack is not empty and the special character has a
                # precedence less than or equal to that of the next character
                # on the stack
                while stack.isEmpty() != True and specials.get(c, 0) <= specials.get(stack.peek(), 0):
			        # pop next character from stack and append to postfix
                    postfix = postfix + stack.pop()
                # and push the character to the stack
                stack.push(c)

            else:
                # just concatenate character to postfix string
                postfix = postfix + c
        
        # loop until stack is empty
        while stack.isEmpty() != True:
            # pop next character from stack and append to postfix
            postfix = postfix + stack.pop()

        # return the postfix string
        return postfix
