/*
2. Escribir un programa en el cual se introduzcan cuatro 
números, calcular y mostrar la suma de los dos primeros
y el producto del tercero y el cuarto.
*/

import java.util.Scanner;

public class Ejercicio2 {

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

        suma = num1 + num2;
        producto = num3 * num4;

        System.out.println("La suma del primer y segundo número es: " + suma);
        System.out.print("El producto del tercer y cuarto número es: " + producto);
    }
}