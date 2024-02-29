
from vector3d import Vector3D
import random

class Estrella:
    nombres_galaxias = ["Andrómeda", "Vía Láctea", "Triángulo", "Magallanes", "Sombrero"]
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = Vector3D(random.uniform(-1000, 1000), random.uniform(-1000, 1000), random.uniform(-1000, 1000))
        self.galaxia = random.choice(Estrella.nombres_galaxias)
    
    def __str__(self):
        return f"Estrella {self.nombre} en {self.posicion}, Galaxia {self.galaxia}"
