# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:52:49 2020

@author: 39333
"""

from functools import reduce
from math import log10

class calculators_functions():
    
    def sum_calc(numbers):
        add =  reduce(lambda x,y: x + y, numbers)
        print('the result is: ', add)
        return add
    
    def subtract_calc(numbers):
        subtract = reduce(lambda x,y: x - y, numbers)
        print('the result is: ', subtract)
        return subtract
    
    def multiply_calc(numbers):
        multiply = reduce(lambda x,y: x * y, numbers)
        print('the result is: ', multiply)
        return multiply
    
    def divide_calc(numbers):
        divide = reduce(lambda x,y: x / y, numbers)
        print('the result is: ', divide)
        return divide
    
    def square_calc(numbers):
        square = (list(map(lambda x: x*x, numbers))[0])
        print('the result is: ', square)
        return square
    
    def square_root(numbers):
        sqrt = (list(map(lambda x: x**0.5, numbers))[0])
        print('the result is: ', sqrt)
        return sqrt
    
    def cube_calc(numbers):
        cube = (list(map(lambda x: x*x*x, numbers))[0])
        print('the result is: ',cube)
        return cube
    
    #factorial function has botha comprehesion list that filter function inside
    def factorial_calc(numbers):
        factorialList = [x  for x in range((numbers[0] + 1))]
        factorial = reduce(lambda x, y: x * y, filter(lambda x: x != 0, factorialList))
        print('the result is: ', factorial)
        return factorial
    
    def geom_mean_calc(numbers):
        geom_m = reduce(lambda x,y: x * y, numbers)**(1/len(numbers))
        print('the geometrical mean of the interval {0} is: {1}'.format(numbers ,
              geom_m))
        return geom_m
    
    def nepero_triplet(numbers):
    #log(a) + log(b) = log(a*b)
        triplet = [(x,y,z) for x in range (1,numbers[0]) for y in range (x,numbers[0]) for z in range (y,numbers[0]) if log10(x) + log10(y) == log10(z)]
        print(list(triplet))
        return triplet

def operation_allowed():
    print("The operations allowed are: \n'1' or '+' for addition,"+
          "\n'2' or '-' for subtraction, "+
          "\n'3' or '*' for moltiplication,"+
          "\n'4' or '/' for division,"+
          "\n'5' or '**' to square a number,"+
          "\n'6' or 'sqrt' to calculate the square root,"+
          "\n'7' or 'cube' to calculate the cube,"+
          "\n'8' or '!' to calculate the factorial,"+
          "\n'9' or 'geom' to calculate the geometrical mean,"+
          "\n'10' or 'nep' to calculate the all the possible triplet" +
          "\n combinations that verify the Nepero rule up to " +
          "the picked number verified (number > 0)")     
    
    
def calculatorInput():
    numbers = []
    numbers.append(eval(input("Please enter a number: ")))    
    operation_allowed()    
    operator_allowed = [ '1', '+','2', '-','3', '*', '4', '/','5', '**',
                        '6', 'sqrt', '7', 'cube', '8', '!','9', 'geom',
                        '10', 'nep']
    
    operator = input("Please enter a operator? ")
    while operator not in operator_allowed:
        print("Please enter a valid operator!".center(4))
        operation_allowed()
        operator = input("Please enter a operator: ")
    if operator in ['1', '+']:
        numbers.append(eval(input("Please enter a number: ")))
        calculators_functions.sum_calc(numbers)
    elif operator in ['2', '-']:
        numbers.append(eval(input("Please enter a number: ")))
        calculators_functions.subtract_calc(numbers)
    elif operator in ['3', '*']:
        numbers.append(eval(input("Please enter a number: ")))
        calculators_functions.multiply_calc(numbers)
    elif operator in ['4', '/']:
        numbers.append(eval(input("Please enter a number: ")))
        calculators_functions.divide_calc(numbers)
    elif operator in ['5', '**']:        
        calculators_functions.square_calc(numbers)
    elif operator in ['6', 'sqrt']:        
        calculators_functions.square_root(numbers)
    elif operator in ['7', 'cube']:
        calculators_functions.cube_calc(numbers)        
    elif operator in ['8', 'factorial']:
        if numbers[0] > 0:
            calculators_functions.factorial_calc(numbers)
        elif numbers[0] == 0:
            print('the result is: ', 1)
        else:            
            while max(numbers) < 0:
                numbers.append(eval(input('Please enter a number >= 0 '+
                                          "Please enter a number: ")))
            new_numbers = max(numbers)
            numbers.clear()
            numbers.append(new_numbers)
            if numbers[0] == 0:
                print('the result is: ', 1)
            else:
                calculators_functions.factorial_calc(numbers)
    elif operator in ['9', 'geom']:
        if max(numbers) <= 0:
            print("Sorry! "+
                  "Geometrical mean can be calculated only for positive numbers." +
                  " All of them must be positive and also to calculte the mean"
                  " are necessary two numbers")
            numbers.clear()
            numbers.append(eval(input('Please enter a number > 0: ')))
            while max(numbers) <= 0 :
                numbers.append(eval(input('Please enter a number > 0: ')))
        numbers = [numbers.pop()]
        print(numbers)
        get_result = 1
        while get_result != 0:
            get_result = eval(input("Please enter another positive number or " +
                                        "type 0 to get the result? "))
            if get_result > 0:
                numbers.append(get_result)
                print(numbers)
            elif get_result == 0:
                if len(numbers) == 0:
                    print("Sorry it is not possible to calculate a geometrical "+
                          "mean for only one number")
                else:
                    calculators_functions.geom_mean_calc(numbers)                  
            else:
                while get_result < 0:
                    get_result = eval(input("The number must be > 0. " +
                                        "Please enter a positive number or " +
                                        "type 0 to get the result? "))
    elif operator in ['10', 'nep']:
        try:
            if numbers[0] < 0:
                while max(numbers) <= 0 :
                    numbers.append(int(input('Please enter a number integer and > 0: ')))
                    numbers[0] = numbers.pop()
                calculators_functions.nepero_triplet(numbers) 
            elif numbers[0] > 0:
                calculators_functions.nepero_triplet(numbers) 
        except:
            print("Number not allowed")         
        
        
def use_calculator_again():
    process_again = ""
    while process_again != "n":
        calculatorInput()
        process_again = input("\n" + "Would you like to use the calculator again (n or to exit)? ")                                     
                
def main():
    use_calculator_again()
    print("bye!")

main()

