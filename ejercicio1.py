class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}"
p = Persona('Alejandro', 20, 'Informático')
print(p.presentarse())