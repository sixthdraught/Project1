from coding import Stack
from coding import FIFO
from coding import OQ

class class_test_stack:
    def __init__(self):
        self.s1 = Stack(10)
        self.s2 = Stack(10)
        self.s3 = Stack(100000)
        self.return_value = True
    def test_pop_push(self):
        self.s1.push(1)
        self.s1.push(2)
        #Test 1
        if not self.s1.pop() == 2:
            print("Test 1 in test_stack failed")
            self.return_value = False  
        self.s1.push(3)
        self.s1.push(4)
        self.s1.push(5)
        #Test 2
        if not self.s1.pop() == 5:
            print("Test 2 in test_stack failed")
            self.return_value = False  
        self.s1.push(4)
        self.s1.push(5)
 
        #self.assertFalse(self.s1.push(3))
        
    def return_bool(self):
        return self.return_value
    
def test_stack():
    s = class_test_stack()
    s.test_pop_push()
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
        
    
    
    

    