
class Galaxia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estrellas = []
    
    def añadir_estrella(self, estrella):
        self.estrellas.append(estrella)
    
    def __str__(self):
        return f"Galaxia {self.nombre} con {len(self.estrellas)} estrellas."
