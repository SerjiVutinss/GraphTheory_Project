# a basic python stack data structure - the end of
# # the inner list property is the top of the stack
class Stack:
    """A basic stack data structure - the end of the inner list property is the top of the stack"""

    def __init__(self):
        # Initialise the inner list
        self.inner_list = []

    def isEmpty(self):
        """Return True if list has items, False if empty"""
        return self.inner_list == []

    def push(self, item):
        """Add an item to the end of the inner list, i.e. top of the stack"""
        self.inner_list.append(item)

    def pop(self):
        """Pop from end of inner list, i.e. top of stack"""
        return self.inner_list.pop()

    def peek(self):
        """Return but do not remove the last item in the inner list, i.e. top of the stack"""
        return self.inner_list[len(self.inner_list) - 1]

    def size(self):
        """Return the number of items in the inner list"""
        return len(self.inner_list)
