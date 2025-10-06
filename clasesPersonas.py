class persona:
    def __init__(self, nom, ap, ed):
        self.nombre = nom
        self.apaterno = ap
        self.edad = ed

    def saludar(self):
       print("Hola, mucho gusto","\nEstoy comiendo")

    def mostrarInfo(self):
        print("Nombre: ",self.nombre,"\nApellido:",self.apaterno,"\nEdad:",self.edad,"\n")


profesor = persona("Gibran","Fuentes",18)
profesor.saludar()
profesor.mostrarInfo()

alumno = persona("Dairi","Reyes",18)
alumno.saludar()
alumno.mostrarInfo()

vendedor = persona("Arial","Bustamante",18)
vendedor.saludar()
vendedor.mostrarInfo()

print(profesor.nombre,profesor.apaterno,profesor.edad)
print(alumno.nombre,alumno.apaterno,alumno.edad)
print(vendedor.nombre,vendedor.apaterno,vendedor.edad)
