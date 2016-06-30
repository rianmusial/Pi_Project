'''
Created on Jun 29, 2016
Last modified on Jun 30, 2016

@author: Rian Musial
'''

from util.numUtil import lowestCommonMultiple, getPrimeFactorization
from copy import deepcopy
from util.root import Root

class Fraction (object):
    def __init__(self, numerator = None, denominator = 1):
        super().__init__()
        
        if isinstance(numerator, float):
            fractionParams = numerator.as_integer_ratio()
            
            self.numerator = fractionParams[0]
            self.denominator = fractionParams[1]
            
            self.denominator *= denominator
            self.simplify()
        
        elif isinstance(numerator, Fraction):
            self.numerator = numerator.numerator
            self.denominator = numerator.denominator
            
            self.denominator *= denominator
        
        else:
            self.numerator = numerator
            self.denominator = denominator
        
    def getNumerator(self):
        return self._numerator
    def setNumerator(self, numerator):
        self._numerator = numerator
    numerator = property(fset = setNumerator, fget = getNumerator)

    def getDenominator(self):
        return self._denominator
    def setDemonimator(self, denominator):
        if(denominator == 0):
            raise ValueError("Denominator cannot be zero.")
        self._denominator = denominator
    denominator = property(fset = setDemonimator, fget = getDenominator)
    
    def simplify(self):
        self.negativeCorrection()
        factors1 = getPrimeFactorization(self.numerator)
        factors2 = getPrimeFactorization(self.denominator)
        
        i = 0
        commonFactors = []
        while i < len(factors1):
            if factors2.count(factors1[i]) > 0:
                commonFactors.append(factors1[i])
                factors2.remove(factors1[i])
                factors1.remove(factors1[i])
                i -= 1
            
            i += 1
    
        commonFactor = 1
        for item in commonFactors:
            commonFactor *= item
            
        self.numerator //= commonFactor
        self.denominator //= commonFactor

    def negativeCorrection(self):
        if self.numerator < 0 and self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
            
        if self.denominator < 0:
            self.denominator = -self.denominator
            self.numerator = -self.numerator

    def flip(self):
        oldNumerator = self.numerator
        oldDenominator = self.denominator
        
        self.numerator = oldDenominator
        self.denominator = oldNumerator
    
    def isInteger(self):
        this = deepcopy(self)
        this.simplify()
        if this.denominator == 1: 
            return True
        else: return False
        
    @staticmethod
    def lowestCommonDenominator(f1, f2):
        if (f1.denominator == f2.denominator): return [f1, f2]
        else:
            return lowestCommonMultiple(f1.denominator, f2.denominator) 
    
    def __float__(self):
        return float(self.numerator)/float(self.denominator)

    def __str__(self, *args, **kwargs):
        retStr = ""
        retStr += str(self.numerator)
        retStr += "/"
        retStr += str(self.denominator)
        return retStr
    
    
    #######################################################
    # Operator overloading
    # 
    # Only implemented for operations on the same type
    #######################################################

    def __int__(self):
        this = deepcopy(self)
        if isinstance(this.numerator, int) and this.denominator == 1:
            return this.numerator
        else:
            errorText = "Fraction "
            errorText += str(self)
            errorText += " cannot be cast to an integer. "
            errorText += "You can round it if an integer is needed."
            raise RuntimeError(errorText)
    
    def __add__(self, other):
        this = deepcopy(self)
        other = deepcopy(other)
        this.simplify()
        other.simplify()
        
        lowestDenom = Fraction.lowestCommonDenominator(this, other)
        
        this.numerator = this.numerator * lowestDenom // this.denominator
        other.numerator = other.numerator * lowestDenom // other.denominator
        
        newNumerator = this.numerator + other.numerator
        newFraction = Fraction(newNumerator, lowestDenom)
        newFraction.simplify()
        return newFraction
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        other = deepcopy(other)
        other.numerator = 0 - other.numerator
        
        return self + other

    def __rsub__(self, other):
        this = -self
        
        return this + other

    def __mul__(self, other):
        this = deepcopy(self)
        other = deepcopy(other)
        
        numerator = this.numerator * other.numerator
        denominator = this.denominator * other.denominator
        
        newFraction = Fraction(numerator, denominator)
        newFraction.simplify()
        return newFraction

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = Fraction(other)
        other.flip()
        
        return self * other
    
    def __rtruediv__(self, other):
        this = deepcopy(self)
        this.flip()
        
        return this * other

    def __floordiv__(self, other):
        return self / other
    
    def __rfloordiv__(self, other):
        return other / self

    def __pow__(self, power):
        this = deepcopy(self)
        for i in range(power - 1):
            this *= self
        
        return this

    def __rpow__(self, other):
        this = Root()
        
        this.degree = self.denominator
        this.multiplicand = 1
        this.radicand = other ** self.numerator
        
        return this

    def __neg__(self):
        negativeLocation = None
        values = [self.numerator, self.denominator]
        for i in range(len(values)):
            if values[i] < 0:
                negativeLocation = i 
        
        this = deepcopy(self)
        this.negativeCorrection()
        
        if negativeLocation == 0:
            this.denominator = 0 - this.denominator
        else:
            this.numerator = 0 - this.numerator

        return this

    def __abs__(self):
        this = deepcopy(self)
        
        this.negativeCorrection()
        if float(this) < 0:
            this.numerator = -this.numerator

        return this

    def __round__(self, n = 0):
        if (n == 0):
            return round(float(self))
        else:
            return round(float(self), n)
        
    def __lt__(self, other):
        this = deepcopy(self)
        other = deepcopy(other)
        
        this.simplify()
        other.simplify()
        
        return float(this) < float(other)
    
    def __le__(self, other):
        this = deepcopy(self)
        other = deepcopy(other)
        
        if this < other:
            return True
        
        elif this == other:
            return True
        
        else: return False

    def __eq__(self, other):
        this = deepcopy(self)
        other = deepcopy(other)
        
        this.simplify()
        other.simplify()
        
        if this.numerator == other.numerator and this.denominator == other.denominator:
            return True
        
        return False

    def __ne__(self, other):
        return (not self == other)
    
    def __gt__(self, other):
        return float(self) > float(other)
    
    def __ge__(self, other):
        if self > other:
            return True
        
        elif self == other:
            return True
        
        else: return False

    def __repr__(self, *args, **kwargs):
        return str(self)
    
def testSuite1():
    f1 = Fraction(1, 2)
    print(float(f1))
    
    f2 = Fraction()
    f2.setNumerator(2)
    f2.setDemonimator(1)
    print(float(f2))
    print(f2)
    
    f3 = f1 + f2
    print (f3)
    
    f4 = f3 - f2
    print (f4)        

def testSuite2():
    f1 = Fraction (10, 2)
    f2 = Fraction (4, 2)
    
    f3 = f1 * f2
    print (f3)
    
    f1 = Fraction(10)
    f3 = f1 / f2
    print(f3)

def testSuite3():
    f = Fraction(1.0)
    print(f)
    
    f1 = Fraction(f, 2)
    print(f1)
    
    f1 = Fraction (2)
    f2 = f1 ** 3
    print (f2) 
    
    f = Fraction(-56, -1)
    print (f)
    f = -f
    print (f)
    
    f = Fraction(5, 2)
    n = round(f, 0)
    
    print(n)

def testSuite4():
    b1 = Fraction(1) < Fraction(2)
    print(b1)
    b2 = Fraction(2) < Fraction (1)
    print(b2)
    b3 = Fraction(2) < Fraction (2)
    print(b3)
        
def main():    
    print("This module has been tested.")

if (__name__ == "__main__"): main()