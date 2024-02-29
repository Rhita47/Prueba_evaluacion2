
class Universo:
    def __init__(self):
        self.galaxias = {}
    
    def añadir_galaxia(self, galaxia):
        if galaxia.nombre not in self.galaxias:
            self.galaxias[galaxia.nombre] = galaxia
        else:
            for estrella in galaxia.estrellas:
                self.galaxias[galaxia.nombre].añadir_estrella(estrella)
    
    def __str__(self):
        return f"Universo con {len(self.galaxias)} galaxias: " + ", ".join([galaxia for galaxia in self.galaxias])
