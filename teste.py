from abc import ABC, abstractmethod

class MultiplicarBase(ABC):
    
    @abstractmethod
    def exec(self, x:int, y:int): pass
    

class Multiplicar(MultiplicarBase):
    
    def exec(self, x, y):
        return (x*y)
    
class LogDecorator(MultiplicarBase):
    def __init__(self, box:MultiplicarBase):
        self.box = box
    
    def exec(self, x, y):
        
        print("CATAPIMBAS")
        
        return self.box.exec(x,y)
    
    
# //////////////////////////////
calc = Multiplicar()
# calc = LogDecorator(calc)
# print(calc.exec(5,4))

assert calc.exec(5,4) == 21