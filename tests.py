from coding import Stack
from coding import FIFO
from coding import OQ

class class_test_stack:
    def __init__(self):
        self.s1 = Stack(5)
        self.s2 = Stack(7)
        self.s3 = Stack(100000)
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
        #self.assertFalse(self.s1.push(3))
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
    def return_bool(self):
        return self.return_value
    
def test_stack():
    s = class_test_stack()
    s.test_pop()
    s.test_push()
    s.pops()
    return s.return_bool()

print(test_stack())

class test_fifo:
     def test_insert_get(self):
        f = FIFO(10)
        f.insert(1)
        f.insert(2)
        f.insert(3)
        self.assertEqual(f.get(), 1)
        self.assertEqual(f.get(), 2)
    
    
class test_oq:
     def test_insert_get_oq(self):
        o = OQ(10)
        o.insert(1)
        o.insert(3)
        o.insert(5)
        o.insert(2)
        o.insert(0.1)
        self.assertEqual(o.get(), 0.1)
        o.get()
        self.assertEqual(o.get(), 2)
        
    
    
    

    