class Felino {
    String tipo;
    double peso;
    int tamano;
    String cor;

    Felino(String tipo, double peso, int tamano, String cor) {
        this.tipo = tipo;
        this.peso = peso;
        this.tamano = tamano;
        this.cor = cor;
    }

    void mostrarInfo() {
        System.out.println(tipo + " " + peso + " " + tamano + " " + cor);
    }
}

public class Felinos { // <- Aquí cambia el nombre
    public static void main(String[] args) {
        Felino gatito = new Felino("gato", 3.6, 25, "Blanco");
        Felino leon = new Felino("leon", 190, 250, "Cafe");
        Felino puma = new Felino("puma", 100, 150, "Negro");

        gatito.mostrarInfo();
        leon.mostrarInfo();
        puma.mostrarInfo();
    }
}
