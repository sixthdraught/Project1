import numpy as np
class Stack:
    #intializing the stack, figuring out whether to use numpy zeros or numpy empty
    def __init__(self, size):
        #crates the numpty array about to be used
        self.stack = np.empty(size)
        #self.top is a running index for the top of the stack, it starts at size - 1 to account for numpy arrays starting at index 0
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
        #self.top provides the index the top of the stack is currently at, the function uses that value to take 
            self.stack[self.top] = val
            self.top -= 1
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
    def __init__(self, size):
        #crates the numpty array about to be used
        self.fifo = np.empty(size)
        #self.first is an index for the front of the queue, it starts at 0 as numpy arrays start at 0 and it 
        #stays 0
        self.first = 0
        #index for where the next value would go if it was inserted
        self.last = 0
        #variable for maxsize, used for debugging
        self.maxsize = size
        #variable for current size
        self.csize = 0
    
    def size(self):
        #simple current size function
        return self.csize
    
    def insert(self, val):
        #checks if the queue is full
        if self.csize == self.maxsize:
            return False
        else:
        #inserts the given value to where self.last points to
            self.fifo[self.last] = val
        #updates self.next
            self.last += 1
        #updates self.csize
            self.csize += 1
            return True

    def get(self):
        #checks if the queue is empty
        if self.csize == 0:
            return None
        else: 
            #removes the first value
            removed_value = self.fifo[self.first]
            #moves the whole queue up by one to compensate for the first value's removal
            for i in range(self.csize):
                if not(i == self.maxsize-1):
                    self.fifo[i] = self.fifo[i+1]
            #updates the last index
            self.last -= 1
            self.fifo[self.last] = None
            #updates the csize count
            self.csize -= 1
            return removed_value
        
        
    def gets(self, val):
        
        pass

    
    #developer commands
    def debug(self):
        #returns useful variables in the specified stack
        return (self.first, self.last, self.maxsize, self.fifo[self.last-1])
    
    def debug2(self):
        #returns all values in the specified queue
        temp = []
        for i in range(self.maxsize):
            temp.append(self.fifo[i])
        return temp    
    
class OQ:
    def __init__(self, val):
        pass

