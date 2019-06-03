import unittest
from greedy_recursive import GreedyRecursive
from greedy_iterative import GreedyIterative

class Greedy_Recursive_testcase(unittest.TestCase):
    def test_greedy_recursive(self):
        start_time=[1,3,0,5,3,5,6,8,8,2,12]
        finish_time=[4,5,6,7,9,9,10,11,12,14,16]
        k=-1
        n=len(start_time)
        Best_result=[0,3,7,10]
        

        self.assertListEqual(GreedyIterative(start_time, finish_time), Best_result)
        self.assertListEqual(GreedyRecursive(start_time, finish_time,k,n), Best_result)

if __name__=='__main__':
    unittest.main()

