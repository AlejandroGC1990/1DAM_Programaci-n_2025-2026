/*
3. Realizar un programa que lea cuatro valores numéricos
y muestre su suma y promedio.
*/
import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] ar) {
        Scanner teclado = new Scanner(System.in);
        int num1, num2, num3, num4, suma, producto;

        System.out.print("Introduce el valor del número 1: ");
        num1 = teclado.nextInt();
        System.out.print("Introduce el valor del número 2: ");
        num2 = teclado.nextInt();
        System.out.print("Introduce el valor del número 3: ");
        num3 = teclado.nextInt();
        System.out.print("Introduce el valor del número 4: ");
        num4 = teclado.nextInt();

        suma = num1 + num2 + num3 + num4;
        producto = num1 * num2 * num3 * num4;

        System.out.println("La suma de los valores es: " + suma);
        System.out.print("El producto de los valores es: " + producto);
    }
}