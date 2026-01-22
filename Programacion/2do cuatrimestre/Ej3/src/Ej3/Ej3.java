package Ej3;

/*Realizar un programa que lea cuatro valores numéricos y muestre su suma y
promedio.
*/

import java.util.Scanner;

public class Ej3 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int v1, v2, v3, v4, suma;
		float promedio;
		
		System.out.print("Ingrese el primer valor: ");
		v1 = teclado.nextInt();
		System.out.print("Ingrese el segundo valor: ");
		v2 = teclado.nextInt();
		System.out.print("Ingrese el tercer valor: ");
		v3 = teclado.nextInt();
		System.out.print("Ingrese el cuarto valor: ");
		v4 = teclado.nextInt();
		
		suma = v1 + v2 + v3 + v4;
		promedio = suma / 4.0f;
		
		System.out.println("La suma de los cuatro valores es: " + suma);
		System.out.println("El promedio de los cuatro valores es: " + promedio);
	}
}
