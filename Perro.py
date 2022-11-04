
from Animal import Animal

class Perro(Animal):
        
    
    def emitir_sonido(self):
        if self.edad<3:
            print("auf auf")
        else:
            if self.edad>=3:
                print("guau guau")