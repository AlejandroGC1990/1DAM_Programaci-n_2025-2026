package ej14;

/*Se introducen por teclado tres números, si todos los valores ingresados son
menores a 10, imprimir en pantalla la leyenda "Todos los números son menores a
diez".*/

import java.util.Scanner;

public class ej14 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		float num1, num2, num3;
		
		System.out.print("Introduce el primer número: ");
		num1 = teclado.nextFloat();
		System.out.print("Introduce el segundo número: ");
		num2 = teclado.nextFloat();
		System.out.print("Introduce el tercer número: ");
		num3 = teclado.nextFloat();
		
		if (num1 < 10 && num2 < 10 && num3 < 10) {
			System.out.println("Todos los número son menores de 10.");
		}
	}
}
