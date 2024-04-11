import unittest
from coding import Stack
from coding import FIFO
from coding import OQ

class test_stack(unittest.TestCase):
    def test_pop_push(self):
        s = Stack(5)
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.pop(), 5)
        s.push(4)
        s.push(5)
        self.assertFalse(s.push(3))
        
class test_fifo(unittest.TestCase):
     def test_insert_get(self):
        f = FIFO(10)
        f.insert(1)
        f.insert(2)
        f.insert(3)
        self.assertEqual(f.get(), 1)
        self.assertEqual(f.get(), 2)
    
    
class test_oq(unittest.TestCase):
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
        
    
    
    
if __name__ == '__main__':
    unittest.main()
    