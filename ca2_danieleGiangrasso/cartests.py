# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:31:16 2020

@author: 39333
"""

import unittest

from carclass import Dealership
from dealershipApp import still_available


class TestDealership(unittest.TestCase):
    
    def setUp(self):
        self.dealership = Dealership()
        
    def test_current_stock(self):        
        self.assertEqual(40, len(self.dealership.create_current_stock()))
        
    def test_process_rental(self):   
        self.assertIn(self.dealership.process_rental(), ['n', 'p','d','e','h'])
                        
class TestDealershipApp(unittest.TestCase):

        
    def test_still_available(self):
        dealership = Dealership()
        car_no_rented = still_available(dealership)
        self.assertLess(len(car_no_rented), 40)  
    

if __name__ == '__main__':
     unittest.main()

        
    
        


