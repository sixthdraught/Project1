import numpy as np
class Stack:
    #intializing the stack, figuring out whether to use numpy zeros or numpy empty
    def __init__(self, size):
        #crates the numpty array about to be used
        self.stack = np.empty(size)
        #self.top is a running index for one above the top of the stack, it starts at size - 1 to account for numpy arrays starting at index 0
        self.top = size - 1
        #variable for maxsize, used for debugging
        self.maxsize = size
        #variable for current size
        self.csize = 0.
    
    def size(self):
        #simple current size function
        return self.csize
    
    def push(self, val):
        #0 is the lowest index value this class will use, -1 indicates the stack is full
        if self.top == -1:
            return False
        else:
        #self.top provides the index for where the new top value should be placed 
            self.stack[self.top] = val
        #updates the top
            self.top -= 1
        #updates the csize
            self.csize += 1
            return True

    def pop(self):
        #checks if the stack is empty
        if self.top == self.maxsize - 1:
            return None
        else: 
            #if this line below just returned the popped value then the 2 lines below it wouldn't work
            #so I saved the value in a temp variable for later use as the top index will change
            popped_value = self.stack[self.top+1]
            #updates the top index
            self.top += 1
            #updates the csize count
            self.csize -= 1
            return popped_value
    def pops(self, val):
        #checks if the value given is an integer and returns a helpful message if it isn't
        if not isinstance(val, int):
            return " the function pops() only accepts integers"
        #checks if the stack is empty
        elif self.top == self.maxsize - 1:
            return []
        #checks for the case where the amount of values to be popped is greater than the current size
        elif self.csize < val:
            temp = []
            #creates a temporary list and then runs a for loop csize times using code from the pop function,
            #appending values popped from the loop to the temp list
            for i in range(self.csize):
                popped_value = self.stack[self.top+1]
                self.top += 1
                self.csize -= 1
                temp.append(popped_value)
            #returns the popped list
            return temp        
        else: 
            temp = []
            #creates a temporary list and then runs a for loop val times using code from the pop function,
            #appending values popped from the loop to the temp list
            for i in range(val):
                popped_value = self.stack[self.top+1]
                self.top += 1
                self.csize -= 1
                temp.append(popped_value)
            return temp
        
        
        
    #developer commands
    def debug(self):
        #returns useful variables in the specified stack
        return (self.top, self.maxsize, self.stack[self.top])
    
    def debug2(self):
        #returns all values in the specified stack
        temp = []
        for i in range(self.maxsize):
            temp.append(self.stack[i])
        return temp

class FIFO:
    def __init__(self, val):
        pass

class OQ:
    def __init__(self, val):
        pass

