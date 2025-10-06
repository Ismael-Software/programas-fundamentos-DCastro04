class car:
    def __init__(self,hp, mdl,vs, col, ns,nd):
        self.horsepower = hp
        self.model = mdl
        self.version = vs
        self.color = col
        self.num_of_seats = ns
        self.num_of_doors = nd
    
    def encender(self):
        print("El auto esta encendido")

    def manejar(self):
        print("El auto esta siendo manejado")

    def acelerar(self):
        print("Acelerando...")

    def frenar(self):
        print("Frenando...")

    def mostrarInfo(self):
        print("Horse power: ",self.horsepower,"\nModelo:",self.model,"\nversion:",self.version,"\nColor:",self.color,"\nNum de asientos:",self.num_of_seats,"\nNum de puertas:",self.num_of_doors,"\n")
 
lamborghini = car(700,"Aventador","SVJ","Verde mantis",2,2)
lamborghini.mostrarInfo()

ferrari = car(600,"458","pista","Rosso corsa",2,2)
ferrari.mostrarInfo()

porsche = car(700,"911","911 GT3 RS","Azul",2,2)
porsche.mostrarInfo()

pagani= car(800,"Zonda","Zonda HP Barchetta","Purple carbon",2,2)
pagani.mostrarInfo()

koegnisegg= car(1000,"Agera RS","Agera RS","Carbon fiber forged",2,2)
koegnisegg.mostrarInfo()

bugatti= car(1500,"Chiron","Super Sport 300+","Blue",2,2)
bugatti.mostrarInfo()

print(lamborghini.horsepower,lamborghini.model,lamborghini.version,lamborghini.color,lamborghini.num_of_seats,lamborghini.num_of_doors)
print(ferrari.horsepower,ferrari.model,ferrari.version,ferrari.color,ferrari.num_of_seats,ferrari.num_of_doors)
print(porsche.horsepower,porsche.model,porsche.version,porsche.color,porsche.num_of_seats,porsche.num_of_doors)
print(pagani.horsepower,pagani.model,pagani.version,pagani.color,pagani.num_of_seats,pagani.num_of_doors)
print(koegnisegg.horsepower,koegnisegg.model,koegnisegg.version,koegnisegg.color,koegnisegg.num_of_seats,koegnisegg.num_of_doors)
print(bugatti.horsepower,bugatti.model,bugatti.version,bugatti.color,bugatti.num_of_seats,bugatti.num_of_doors)