import java.util.Scanner;

public class PruebaVector2 {
    // Definimos los atributos como 'private' (Encapsulamiento)
    private Scanner teclado;
    private float[] alturas;
    private float promedio;

    public void cargar() {
        teclado = new Scanner(System.in);
        alturas = new float[5]; // Creamos el vector de 5 posiciones
        for (int f = 0; f < 5; f++) {
            System.out.print("Introduce la altura de la persona " + (f + 1) + ": ");
            alturas[f] = teclado.nextFloat();
        }
    }

    public void calcularPromedio() {
        float suma = 0;
        for (int f = 0; f < 5; f++) {
            suma = suma + alturas[f]; // Sumamos lo que hay en cada "cajón"
        }
        promedio = suma / 5;
        System.out.println("Promedio de alturas: " + promedio);
    }

    public void mayoresMenores() {
        int may = 0, men = 0;
        for (int f = 0; f < 5; f++) {
            if (alturas[f] > promedio) {
                may++;
            } else if (alturas[f] < promedio) {
                men++;
            }
        }
        System.out.println("Cantidad de personas mayores al promedio: " + may);
        System.out.println("Cantidad de personas menores al promedio: " + men);
    }

    public static void main(String[] ar) {
        PruebaVector2 pv2 = new PruebaVector2();
        pv2.cargar();
        pv2.calcularPromedio();
        pv2.mayoresMenores();
    }
}