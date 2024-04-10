import numpy as np
class Stack:
    #intializing the stack, figuring out whether to use numpy zeros or numpy empty
    def __init__(self, size):
        #crates the numpty array about to be used
        self.stack = np.empty(size)
        #self.top is a running index for one above the top value of the stack, it starts at size - 1 to account for numpy arrays starting at index 0
        self.top = size - 1
        #variable for maxsize, used for debugging
        self.maxsize = size
        #variable for current size
        self.csize = 0
    
    def size(self):
        #simple current size function
        return self.csize
    
    def push(self, val):
        #0 is the lowest index value this class will use(the highest point of the stack), -1 indicates the stack is full
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
    def __init__(self, size):
        #creates the numpty array about to be used
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
        #checks for the empty case
        if self.csize == 0:
            return []
        elif val > self.csize:
            #temporary list that will be returned at the end of the function
            temp = []
            #iterates this block over the whole queue as the given value is too big
            for i in range(self.csize):
                #stores the first value before it's modified by the next for loop
                removed_value = self.fifo[self.first]
                #loop that shifts the whole queue up by one to account for numpy arrays
                #having a fixed size
                for i in range(self.csize):
                    #checks for the case where the resulting index called by i+1 is out of bounds
                    if not(i == self.maxsize-1):
                        #shifts the selected index up by 1
                        self.fifo[i] = self.fifo[i+1]
                #takes the stored value and appends it to a list to return to the user later
                temp.append(removed_value)
                #updates the last index
                self.last -= 1
                #accounts for the last value not being removed by the previous for loop
                self.fifo[self.last] = None
                #updates the csize count
                self.csize -= 1
            return temp
        else:
            #temporary list that will be returned at the end of the function
            temp = []
            #iterates this block over the given int to return the requested number of values from the queue
            for i in range(val):
                #stores the first value before it's modified by the next for loop
                removed_value = self.fifo[self.first]
                #loop that shifts the whole queue up by one to account for numpy arrays
                #having a fixed size
                for i in range(self.csize):
                    #checks for the case where the resulting index called by i+1 is out of bounds
                    if not(i == self.maxsize-1):
                        #shifts the selected index up by 1
                        self.fifo[i] = self.fifo[i+1]
                #takes the stored value and appends it to a list to return to the user later
                temp.append(removed_value)
                #updates the last index
                self.last -= 1
                #accounts for the last value not being removed by the previous for loop
                self.fifo[self.last] = None
                #updates the csize count
                self.csize -= 1
            return temp
    
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
    def __init__(self, size):
        #creates the numpty array about to be used
        if isinstance(size, int):
            if size > 0:
                self.oq = np.empty(size)
        #self.first is an index for the front of the queue, it starts at 0 as numpy arrays start at 0 and it 
        #stays 0
                self.first = 0
        #keeps track of the back of the queue
                self.last = 0
        #variable for maxsize, used for debugging
                self.maxsize = size
        #variable for current size
                self.csize = 0
        else:
            raise "enter an integer value greater than 0 to initialize the ordered queue"
    
    def size(self):
        #simple current size function
        return self.csize
    
    def insert(self, val):
        #checks if the queue is full
        if not (isinstance(val, (float, int))):
            return "ordered queues can only contain numbers"
        #checks if OQ is full
        elif self.csize == self.maxsize:
            return False
        #makes sure the OQ isn't empty
        elif self.csize > 0:
        #iterates the forecoming code to make sure 
            for i in range(self.csize):
                if val < self.oq[i]:
                    temp = i
                    for i_2 in reversed(range(i, self.csize)):
                        self.oq[i_2+1] = self.oq[i_2]
                    self.oq[temp] = val
                    self.csize += 1
                    return True
    
            self.oq[self.csize] = val
            self.csize += 1
            return True
        elif self.csize == 0:
            self.oq[self.first] = val  
            self.csize += 1  
            return True
        
        #developer commands
    def debug(self):
        #returns useful variables in the specified stack
        return (self.csize, self.maxsize, self.debug2())
    
    def debug2(self):
        #returns all values in the specified queue
        temp = []
        for i in range(self.maxsize):
            temp.append(self.oq[i])
        return temp    
    

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
        #checks for the empty case
        if self.csize == 0:
            return []
        elif val > self.csize:
            #temporary list that will be returned at the end of the function
            temp = []
            #iterates this block over the whole queue as the given value is too big
            for i in range(self.csize):
                #stores the first value before it's modified by the next for loop
                removed_value = self.fifo[self.first]
                #loop that shifts the whole queue up by one to account for numpy arrays
                #having a fixed size
                for i in range(self.csize):
                    #checks for the case where the resulting index called by i+1 is out of bounds
                    if not(i == self.maxsize-1):
                        #shifts the selected index up by 1
                        self.fifo[i] = self.fifo[i+1]
                #takes the stored value and appends it to a list to return to the user later
                temp.append(removed_value)
                #updates the last index
                self.last -= 1
                #accounts for the last value not being removed by the previous for loop
                self.fifo[self.last] = None
                #updates the csize count
                self.csize -= 1
            return temp
        else:
            #temporary list that will be returned at the end of the function
            temp = []
            #iterates this block over the given int to return the requested number of values from the queue
            for i in range(val):
                #stores the first value before it's modified by the next for loop
                removed_value = self.fifo[self.first]
                #loop that shifts the whole queue up by one to account for numpy arrays
                #having a fixed size
                for i in range(self.csize):
                    #checks for the case where the resulting index called by i+1 is out of bounds
                    if not(i == self.maxsize-1):
                        #shifts the selected index up by 1
                        self.fifo[i] = self.fifo[i+1]
                #takes the stored value and appends it to a list to return to the user later
                temp.append(removed_value)
                #updates the last index
                self.last -= 1
                #accounts for the last value not being removed by the previous for loop
                self.fifo[self.last] = None
                #updates the csize count
                self.csize -= 1
            return temp