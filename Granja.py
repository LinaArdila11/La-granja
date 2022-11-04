from Animal import Animal
from Bovino import Bovino
from Perro import Perro

class Granja:
    def __init__(self):
        self.Perros=[]
        self.Bovivos=[]
    

    def agregar_Perro(self, edad, raza, peso, propietario, fecha):
        misPerros=Perro()
        misPerros.edad=edad
        misPerros.raza=raza
        misPerros.peso=peso
        misPerros.fecha_vacunacion=fecha
        misPerros.propietario=propietario
         
    def agregar_Bovino(self, edad, raza, peso, propietario,fecha):
        misBovinos=Bovino()
        misBovinos.edad=edad
        misBovinos.raza=raza
        misBovinos.peso=peso
        misBovinos.fecha_vacunacion=fecha
        misBovinos.propietario=propietario
    def obtener_Perros(self,id):
        return self.Perros[id]
        
    def obtener_Bovinos(self,id):
        return self.Bovivos[id]


