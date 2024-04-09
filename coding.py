import numpy as np
class Stack:
    #intializing the stack, figuring out whether to use numpy zeros or numpy empty
    def __init__(self, size):
        #crates the numpty array about to be used
        self.stack = np.empty(size)
        #self.top is a running index for the top of the stack; index starts with 0
        self.top = size - 1
        self.maxsize = size
        self.size = 0
    
    def size(self):
        return self.size
    
    def push(self, val):
        if self.top == -1:
            return False
        else:
            self.stack[self.top] = val
            self.top -= 1
            self.size += 1
            return True

    def pop(self):
        if self.top == self.size - 1:
            return None
        else: 
            #if this line below just returned the popped value then the 2 lines below it wouldn't work
            #so I saved the value in a temp variable for later use as the top index will change
            popped_value = self.stack[self.top+1]
            self.top += 1
            self.size -= 1
            return popped_value
    
    
    
            
    
    def debug(self):
        return (self.top, self.maxsize, self.stack[self.top])
    
    def debug2(self):
        temp = []
        for i in range(self.size):
            temp.append(self.stack[i])
        return temp


