'''
Created on Jun 30, 2016
Last modified on Jun 30, 2016

@author: Rian Musial
'''

from copy import deepcopy, copy
from util.root import Root

class CompositeRoot(object):
    def __init__(self, *args):
        super().__init__()
        self.roots = []
        
        for i in args:
            self.add(i)
        
    def getRoots(self):
        return self._roots
    def setRoots(self, roots):
        self._roots = roots
    roots = property(fset = setRoots, fget = getRoots)
    
    def add(self, obj):
        obj = deepcopy(obj)
        
        if isinstance(obj, int):
            obj = Root(obj)
        elif isinstance(obj, CompositeRoot):
            for i in obj.roots:
                self.add(i)
            return
        
        itemFound = False
        for i in range(len(self.roots)):
            if self.roots[i].radicand == obj.radicand and self.roots[i].degree == obj.degree:
                itemFound = True
                self.roots[i].multiplier += obj.multiplier
        
        if not itemFound:
            self.roots.append(obj)
    
    def __str__(self):
        retStr = ""
        if len(self.roots) > 1: retStr += "("
        for i in range(len(self.roots)):
            retStr += str(self.roots[i])
            try:
                self.roots[i + 1]
                retStr += " + "
            except:
                pass
        if len(self.roots) > 1: retStr += ")"
        
        return retStr
    
    def __float__(self):
        floatOut = 0.0
        for i in self.roots:
            floatOut += float(i)
        return floatOut

    def __add__(self, other):
        this = deepcopy(self)
        this.add(other)
        
        if len(this.roots) == 1:
            return this.roots[0]
        
        return this
    
    def __radd__(self, other):
        return self + other
    
    def __neg__(self):
        this = deepcopy(self)
        
        for i in range(len(this.roots)):
            this.roots[i] = -this.roots[i]
            
        return this
    
    def __sub__(self, other):
        other = -other
        
        return self + other
    
    def __rsub__(self, other):
        this = -self
        
        return this + other  

def testSuite1():
    r1 = Root(5, 2)
    r2 = Root(2, 9, 3)
    
    c = CompositeRoot()
    c.roots.append(deepcopy(r1))
    c.roots.append(deepcopy(r2))
    
    print(c)
    
    print(float(r1))
    print(float(r2))
    print(c)
    print(float(r1) + float(r2))
    print(float(c))
    
    r1 = deepcopy(r1)
    r2 = deepcopy(r2)
    c1 = CompositeRoot(r1, r2)
    print(c)
    print(c1)

def testSuite2():
    r1 = Root(1)
    c2 = CompositeRoot(r1, r1)
    print(r1)
    print(c2)
    c3 = c2 + r1
    
    print(c3)

def testSuite3():
    pass
    
def main():
    testSuite3()

if __name__ == "__main__": main()