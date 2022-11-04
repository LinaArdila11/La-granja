

class Animal:

    def __init__(self):
        self.peso=" "
        self.edad=" "
        self.raza=""
        self.propietario=" "
        self.fecha_vacunacion=" "

    def correr(self):
        if self.edad<5:
            print("LENTO")
        else:
            if self.edad>=5:
                print("RAPIDO")

    def emitir_sonido(self):
        if self.edad<3:
            print("auf auf")
        else:
            if self.edad>=3:
                print("guau guau")
            
    def obtener_edad(self):
        self.edad=int(input("INGRESE LA EDAD DE ANIMAL:"))


    
