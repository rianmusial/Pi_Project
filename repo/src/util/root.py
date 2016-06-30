'''
Created on Jun 29, 2016
Last modified Jun 29, 2016

@author: Rian Musial
'''
class Root (object):
    def __init__(self, radicand = None, degree = 1, multiplicand = 1):
        super().__init__()
        
        self.radicand = radicand
        self.degree = degree
        self.multiplicand = multiplicand
        
    def getDegree(self):
        return self._degree
    def setDegree(self, degree):
        self._degree = degree
    degree = property(fset = setDegree, fget = getDegree)
    
    def getRadicand(self):
        return self._radicand
    def setRadicand(self, radicand):
        self._radicand = radicand
    radicand = property(fset = setRadicand, fget = getRadicand)
    
    def getMultiplicand(self):
        return self._multiplicand
    def setMultiplicand(self, multiplicand):
        self._multiplicand = multiplicand
    multiplicand = property(fset = setMultiplicand, fget = getMultiplicand)
    multiplier = property(fset = setMultiplicand, fget = getMultiplicand)
    
    def __str__(self, *args, **kwargs):
        retStr = ""
        retStr += str(self.multiplicand)
        retStr += "*"
        retStr += str(self.degree)
        retStr += "^⎷"
        retStr += str(self.radicand)
        
        return retStr
    
    def __float__(self):
        radicand = float(self.radicand)
        multiplier = float(self.multiplicand)
        degree = float(self.degree) 
        return multiplier * (radicand ** (1 / degree))
    
def main():
    r = Root(1)
    print(r)
    print(float(r))
    
    r = Root(4, 2)
    print(r)
    print(float(r))
    
    r = Root(93, 9, 3)
    print(r)
    print(float(r))

if __name__ == "__main__": main()