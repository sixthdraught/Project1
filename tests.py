from coding import Stack
from coding import FIFO
from coding import OQ

class class_test_stack:
    def __init__(self):
        self.s1 = Stack(5)
        self.s2 = Stack(7)
        self.s3 = Stack(10)
        self.s4 = Stack(10)
        self.return_value = True
    def test_pop(self):
        self.s1.push(1)
        self.s1.push(2)
        #Test 1
        #simple test to see if pop is returning the last value put in
        if not self.s1.pop() == 2:
            print("Test 1 in test_stack failed")
            self.return_value = False  
        self.s1.push(3)
        self.s1.push(4)
        self.s1.push(5)
        #Test 2
        #simple test to see if pop is returning the last value put in
        if not self.s1.pop() == 5:
            print("Test 2 in test_stack failed")
            self.return_value = False  
        self.s1.push(4)
        self.s1.push(5)
    def test_push(self):
        #Test 3
        #checks if push realizes the stack is full
        if not self.s1.push(20) == False:
            print("Test 3 in test_stack failed")
            self.return_value = False 
        self.s1.pop()
        self.s1.push("hi")
        #Test 4
        #checks if push can take strings
        if not self.s1.pop() == "hi":
            print("Test 4 in test_stack failed")
            self.return_value = False 
    def pops(self):
        self.s2.push(1)
        self.s2.push(2)
        self.s2.push(3)
        self.s2.push(4)
        self.s2.push(5)
        self.s2.push(6)
        self.s2.push(7)
        #Test 5      
        #checks if pops works as intended  
        if not self.s2.pops(7) == [7,6,5,4,3,2,1]:
            print("Test 5 in test_stack failed")
            self.return_value = False 
        #Test 6
        #checks if pops returns en empty list when used on an empty stack
        if not self.s2.pops(5) == []:
            print("Test 6 in test_stack failed")
            self.return_value = False 
    def property_testing(self):
        self.s3.push(1)
        self.s3.push(2)
        self.s3.push(10)
        for i in (range(10)):
            self.s4.push(i+1)
        if not self.s3.pop() == self.s4.pop():
            print("Test 7 in test_stack failed")
            self.return_value = False
        
    def return_bool(self):
        return self.return_value

class class_test_queue:
    def __init__(self):
        self.s1 = FIFO(5)
        self.s2 = FIFO(7)
        self.s3 = FIFO(10)
        self.s4 = FIFO(10)
        self.return_value = True
    def test_insert(self):
        self.s1.insert(1)
        self.s1.insert(2)
        #Test 1
        #simple test to see if get is returning the first value put in
        if not self.s1.get() == 1:
            print("Test 1 in test_queue failed")
            self.return_value = False  
        self.s1.insert(3)
        self.s1.insert(4)
        self.s1.insert(5)
        #Test 2
        #simple test to see if get is returning the first value put in
        if not self.s1.get() == 2:
            print("Test 2 in test_queue failed")
            self.return_value = False  
        self.s1.insert("hi")
        self.s1.insert(4)
        self.s1.insert(5)
    def test_get(self):
        #Test 3
        #checks if insert realizes the queue is full
        if not self.s1.insert(20) == False:
            print("Test 3 in test_queue failed")
            self.return_value = False 
        self.s1.get()
        self.s1.get()
        self.s1.get()
        #Test 4
        #checks if insert can take strings
        if not self.s1.get() == "hi":
            print("Test 4 in test_queue failed")
            self.return_value = False 
    def test_gets(self):
        self.s2.insert(1)
        self.s2.insert(2)
        self.s2.insert(3)
        self.s2.insert(4)
        self.s2.insert(5)
        self.s2.insert(6)
        self.s2.insert(7)
        #Test 5      
        #checks if gets works as intended  
        if not self.s2.gets(7) == [1,2,3,4,5,6,7]:
            print("Test 5 in test_queue failed")
            self.return_value = False 
        #Test 6
        #checks if gets returns en empty list when used on an empty queue
        if not self.s2.gets(5) == []:
            print("Test 6 in test_queue failed")
            self.return_value = False 
    def property_testing(self):
        self.s3.insert(1)
        self.s3.insert(2)
        self.s3.insert(10)
        for i in (range(10)):
            self.s4.insert(i+1)
        if not self.s3.get() == self.s4.get():
            print("Test 7 in test_queue failed")
            self.return_value = False
    def return_bool(self):
        return self.return_value
    
class class_test_oq:
    def __init__(self):
        self.s1 = OQ(10)
        self.s2 = OQ(10)
        self.s3 = OQ(10)
        self.s4 = OQ(10)
        self.return_value = True
        
    #Test 1
    #Tests if the OQ successfully orders the list
    def property_testing(self):
        self.s3.insert(1)
        self.s3.insert(2)
        self.s3.insert(10)
        self.s3.insert(3)
        self.s3.insert(5)
        self.s3.insert(7)
        self.s3.insert(6)
        self.s3.insert(9)
        self.s3.insert(8)
        self.s3.insert(4)
        for i in (range(10)):
            self.s4.insert(i+1)
        if not self.s3.gets(10) == self.s4.gets(10):
            print("Test 1 in test_oq failed")
            self.return_value = False
            
    def return_bool(self):
        return self.return_value
    
def test_stack():
    s = class_test_stack()
    s.test_pop()
    s.test_push()
    s.pops()
    s.property_testing()
    return s.return_bool()

def test_queue():
    q = class_test_queue()
    q.test_insert()
    q.test_get()
    q.test_gets()
    q.property_testing()
    return q.return_bool()

def test_oq():
    oq = class_test_oq()
    oq.property_testing()
    return oq.return_bool()

def test_all():
    print(test_stack())
    print(test_queue())
    print(test_oq())
test_all()