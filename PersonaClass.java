class Persona {
    String nombre;
    String apaterno;
    int edad;

    // Constructor
    Persona(String nom, String ap, int ed) {
        this.nombre = nom;
        this.apaterno = ap;
        this.edad = ed;
    }

    void saludar() {
        System.out.println("Hola, mucho gusto\nEstoy comiendo");
    }

    void mostrarInfo() {
        System.out.println("Nombre: " + this.nombre +
                           "\nApellido: " + this.apaterno +
                           "\nEdad: " + this.edad + "\n");
    }
}

public class PersonaClass {
    public static void main(String[] args) {
        Persona profesor = new Persona("Gibran", "Fuentes", 18);
        profesor.saludar();
        profesor.mostrarInfo();

        Persona alumno = new Persona("Dairi", "Reyes", 18);
        alumno.saludar();
        alumno.mostrarInfo();

        Persona vendedor = new Persona("Arial", "Bustamante", 18);
        vendedor.saludar();
        vendedor.mostrarInfo();

        System.out.println(profesor.nombre + " " + profesor.apaterno + " " + profesor.edad);
        System.out.println(alumno.nombre + " " + alumno.apaterno + " " + alumno.edad);
        System.out.println(vendedor.nombre + " " + vendedor.apaterno + " " + vendedor.edad);
    }
}
