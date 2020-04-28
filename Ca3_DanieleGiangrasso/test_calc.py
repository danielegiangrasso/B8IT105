# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:39:17 2018

@author: 99993
"""

import unittest

from Calculator import calculators_functions
#add, divide, exponent, multiply, subtract


class FunctionTest(unittest.TestCase):
    
    functions = calculators_functions()

    def testSum(self):  
        self.assertEqual(4, calculators_functions.sum_calc([2,2]))
        self.assertEqual(5, calculators_functions.sum_calc([2,3]))
    
    def testSubtract(self):  
        self.assertEqual(0, calculators_functions.subtract_calc([2,2]))
        self.assertEqual(-1, calculators_functions.subtract_calc([2,3]))
    
    def testMultiply(self):  
        self.assertEqual(0, calculators_functions.multiply_calc([0,2,0]))
        self.assertEqual(-1, calculators_functions.multiply_calc([2,3,-(1/6)]))
 
    def testDivide(self):
        self.assertTrue(2, int(calculators_functions.divide_calc([2, 1])))
        self.assertGreater(calculators_functions.divide_calc([3, 1]), calculators_functions.divide_calc([2, 1]))

    def testSq(self):  
        self.assertTrue(calculators_functions.square_calc([6]),2)
    
    def testSqrt(self):  
        self.assertEqual(2, calculators_functions.square_root([4]))
        self.assertEqual(2.449489742783178, calculators_functions.square_root([6]))  
   
    def testCube(self):  
        self.assertEqual( -64 ,calculators_functions.cube_calc([-4]))
        self.assertEqual(abs(calculators_functions.cube_calc([-3])), calculators_functions.cube_calc([3]))

    def testFactorial(self):  
        self.assertEqual(6,calculators_functions.factorial_calc([3]))
        self.assertIn(calculators_functions.factorial_calc([3]), range(100))
    
    def testGeomMean(self):
        self.assertGreater(calculators_functions.geom_mean_calc([1, 2, 4]), calculators_functions.geom_mean_calc([1, 2, 3]))
        self.assertEqual(1,calculators_functions.geom_mean_calc([1, 1, 1, 1, 1]))

    def testNepero(self):
        self.assertEqual( [] ,list(calculators_functions.nepero_triplet([0])))
        self.assertGreater( len(calculators_functions.nepero_triplet([30])),len(calculators_functions.nepero_triplet([29])))        

if __name__ == '__main__':
     unittest.main()


