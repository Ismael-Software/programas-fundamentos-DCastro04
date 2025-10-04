class Felino:
    def __init__(self, tipo, peso, tamano, cor):
        self.tipo = tipo
        self.peso = peso
        self.tamano = tamano
        self.cor = cor

# Creación de objetos
gatito = Felino("gato", 3.6, 25, "Blanco")
leon = Felino("leon", 190, 250, "Cafe")
puma = Felino("puma", 100, 150, "Negro")


print(gatito.tipo,gatito.peso,gatito.tamano,gatito.cor)
print(leon.tipo,leon.peso,leon.tamano,leon.cor)
print(puma.tipo,puma.peso,puma.tamano,puma.cor)
