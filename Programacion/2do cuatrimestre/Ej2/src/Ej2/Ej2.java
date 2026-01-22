package Ej2;

/*Escribir un programa en el cual se introduzcan cuatro números, calcular y
mostrar la suma de los dos primeros y el producto del tercero y el cuarto.*/

import java.util.Scanner;

public class Ej2 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int num1, num2, num3, num4, suma, producto;
		
		System.out.print("Introduce el primer número: ");
		num1 = teclado.nextInt();
		System.out.print("Introduce el segundo número: ");
		num2 = teclado.nextInt();
		System.out.print("Introduce el tercer número: ");
		num3 = teclado.nextInt();
		System.out.print("Introduce el cuarto número: ");
		num4 = teclado.nextInt();
		
		suma = num1 + num2;
		producto = num3 * num4;
		
		
		System.out.println("La suma de los priemros número es " + suma);
		System.out.println("El producto de los dos siguientes números es " + producto);
	}
}
