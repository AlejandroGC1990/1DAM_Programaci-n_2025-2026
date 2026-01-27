package ej10;

/*Confeccionamos un programa que permita cargar un número entero positivo de
 hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar
 un mensaje de error si el número de cifras es mayor*/

import java.util.Scanner;

public class ej10 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int num;
		
		System.out.print("Introduce un valor: ");
		num = teclado.nextInt();
		
		if (num < 10) {
			System.out.println("El número tiene 1 cifra");
		}
		else {
			if (num < 100) {
				System.out.println("El número tiene 2 cifras");
			}
			else {
				if (num < 1000) {
					System.out.println("El número tiene 3 cifras");
				}
				else {
					System.out.println("Error. El número tiene más de 4 cifras");
				}
			}
		}
	}
}
