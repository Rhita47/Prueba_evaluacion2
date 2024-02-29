import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Estrella ubicada en ({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        if abs(self.x) > 5000 or abs(self.y) > 5000 or abs(self.z) > 5000:
            return "Galaxia Lejana"
        else:
            return "Vía Láctea"
    
    def distancia(self, otra):
        return math.sqrt((self.x - otra.x)**2 + (self.y - otra.y)**2 + (self.z - otra.z)**2)
    

estrella_a = Estrella(2, 3, 1)
estrella_b = Estrella(4, 4, 4)
estrella_c = Estrella(-3, -1, 0)

estrellas = [estrella_a, estrella_b, estrella_c]

for estrella in estrellas:
    print(estrella)
    print(f"Galaxia: {estrella.galaxia()}")

print(f"Distancia entre A y B: {estrella_a.distancia(estrella_b)}")
print(f"Distancia entre B y C: {estrella_b.distancia(estrella_c)}")


origen = Estrella(0, 0, 0)

distancias = {estrella: origen.distancia(estrella) for estrella in estrellas}
estrella_mas_lejana = max(distancias, key=distancias.get)

print(f"La estrella más lejos del origen es: {estrella_mas_lejana}")

