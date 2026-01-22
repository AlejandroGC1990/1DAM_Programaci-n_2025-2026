package ej8;

/*Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de
 ellos.*/

import java.util.Scanner;

public class ej8 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		float num1, num2, num3;
		
		System.out.print("Introduce el primer número: ");
		num1 = teclado.nextFloat();
		System.out.print("Introduce el segundo número: ");
		num2 = teclado.nextFloat();
		System.out.print("Introduce el tercer número: ");
		num3 = teclado.nextFloat();
		
		if (num1 > num2 && num1 > num3) {
			System.out.println("El mayor número es " + num1);
		}
		else {
			if (num2 > num1 && num2 > num3) {
				System.out.println("El mayor número es " + num2);
			}
			else {
				System.out.println("El mayor número es " + num3);
			}
		}
	}
}
