'''
Created on Jun 29, 2016
Last modified Jun 30, 2016

@author: Rian Musial
'''

from copy import deepcopy

class Root (object):
    def __init__(self, radicand = None, degree = 1, multiplicand = 1):
        super().__init__()
        
        self.radicand = radicand
        self.degree = degree
        self.multiplicand = multiplicand
        
    def getDegree(self):
        return self._degree
    def setDegree(self, degree):
        if degree == 0:
            raise ValueError("Degree of a root cannot be zero.")
        self._degree = degree
    degree = property(fset = setDegree, fget = getDegree)
    
    def getRadicand(self):
        return self._radicand
    def setRadicand(self, radicand):
        if radicand < 0:
            raise ValueError("Radicand cannot be less than zero.")
        self._radicand = radicand
    radicand = property(fset = setRadicand, fget = getRadicand)
    
    def getMultiplicand(self):
        return self._multiplicand
    def setMultiplicand(self, multiplicand):
        self._multiplicand = multiplicand
    multiplicand = property(fset = setMultiplicand, fget = getMultiplicand)
    multiplier = property(fset = setMultiplicand, fget = getMultiplicand)

    def isInteger(self):
        if self.degree == 1:
            return True
        elif self._hasRoot():
            return True
        else:
            return False
        
    def _hasRoot(self):
        for i in range(self.radicand):
            x = i ** self.degree
            if x == self.radicand:
                return True
        
        return False
        
    def _toInteger(self):
        if not self.isInteger():
            errorText = "Cannot cast Root "
            errorText += str(self)
            errorText += " as Integer."
            raise ValueError(errorText)
        if self.degree == 1:
            return self.multiplicand * self.radicand
        else:
            intOut = 1
            intOut *= int(self.radicand ** (1 / self.degree))
            intOut *= self.multiplier
            
            return intOut
    
    def __str__(self, *args, **kwargs):
        if self.degree == 1 and self.radicand == 1:
            return str(self.multiplicand)
        
        elif self.degree == 1:
            return str(self.multiplicand * self.radicand)
        
        else:
            retStr = ""
            retStr += str(self.multiplicand)
            retStr += "*"
            retStr += str(self.degree)
            retStr += "^/"
            retStr += str(self.radicand)
            
            return retStr
    
    def __float__(self):
        tempRadicand = float(self.radicand)
        tempMultiplier = float(self.multiplicand)
        tempDegree = float(self.degree) 
        return tempMultiplier * (tempRadicand ** (1 / tempDegree))

    def __int__(self):
        return self._toInteger()

    def __add__(self, other):
        from util.compositeRoot import CompositeRoot
        this = CompositeRoot(self)
        other = CompositeRoot(other)
        
        added = this + other
        return added
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        other = -other
        return self + other
    
    def __rsub__(self, other):
        this = -self
        return this + other
    
    def __mul__(self, other):
        return NotImplemented
    def __rmul__(self, other):
        return NotImplemented
    def __truediv__(self, other):
        return NotImplemented
    def __rtruediv__(self, other):
        return NotImplemented
    
    def __floordiv__(self, other):
        return self / other
    def __pow__(self, other):
        this = deepcopy(self)
        this.multiplicand **= other
        this.degree = this.degree % other
        if self.degree < other:
            times = self.degree // other
            this.multiplicand = this.multiplicand * (self.radicand * times)
        if self.degree == 0:
            return this.multiplicand
        elif self.degree == 1:
            return this.multiplicand * this.radicand
        else:
            return this
    
    def __rpow__(self, other):
        return NotImplemented
    
    def __neg__(self):
        this = deepcopy(self)
        this.multiplicand = -this.multiplicand
        return this
    
    def __abs__(self):
        this = deepcopy(self)
        this.multiplicand = abs(this.multiplicand)
        return this
    
    def __round__(self):
        return round(float(self))
    
def testSuite1():
    r = Root(1)
    print(r)
    print(float(r))
    
    r = Root(4, 2)
    print(r)
    print(float(r))
    
    r = Root(93, 9, 3)
    print(r)
    print(float(r))
    print(type(r))
    print(isinstance(r, Root))
    
def testSuite2():
    r = Root(1)
    print(int(r))
    
    r1 = Root(2)
    r2 = Root(4, 2)
    i1 = int(r1) + int(r2)
    r3 = r1 + r2
    print(i1)
    print(r3)

def main():
    testSuite2()

if __name__ == "__main__": main()