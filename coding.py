import numpy as np
class Stack:
    #intializing the stack, figuring out whether to use numpy zeros or numpy empty
    def __init__(self, size):
        #crates the numpty array about to be used
        self.stack = np.empty(size)
        #self.top is a running index for the top of the stack; index starts with 0
        self.top = size - 1
    
    def push(self, val):
        self.stack[self.top] = val
        self.top -= 1

    def pop(self):
        self.top += 1
        return self.stack[self.top]
        
    




