from Animal import Animal

class Bovino(Animal):

    def __init__(self):
        self.propietario=" "
        self.fecha_vacunacion=" "
        self.establo=0

    def Pastar(self):
        if self.establo<=5:
            print("NO pastar")
        else:
            if self.establo>5:
                print ("Pastar")
    def emitir_sonido(self):
        print("MUUUUUUUUU")