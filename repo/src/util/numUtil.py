'''
Created on Jun 29, 2016
Last modified on Jun 29, 2016

@author: Rian Musial
'''

def lowestCommonMultiple(num1, num2):
    if num1 % num2 == 0: return num1
    elif num2 % num1 == 0: return num2
    else:
        factor1 = getPrimeFactorization(num1)
        factor2 = getPrimeFactorization(num2)
        
        for number in factor1:
            if factor2.count(number) > 0:
                factor2.remove(number)
        
        for number in factor2:
            factor1.append(number)
            
        multiple = 1
        for number in factor1:
            multiple *= number
            
        return multiple

def getPrimeFactorization(intIn):
    valuesOut = []
    tempInt = intIn
    
    for i in primeNumbers(intIn):
        while(tempInt % i == 0):
            valuesOut.append(i)
            tempInt /= i
    
    if valuesOut == []: valuesOut.append(intIn)
    return valuesOut
    
def primeNumbers(intIn):
    divisorFound = False
    
    for i in range(2, intIn):
        divisorFound = False
        
        for j in range(2, i):
            if (i % j == 0):
                divisorFound = True
        
        if divisorFound == False:
            yield i
    
def main():
    print("This module has been tested.")
    
if __name__ == "__main__": main()