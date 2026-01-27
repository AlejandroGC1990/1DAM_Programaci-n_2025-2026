package ej15;

/*Se introducen por teclado tres números, si al menos uno de los valores
ingresados es menor a 10, imprimir en pantalla la leyenda "Alguno de los números
es menor a diez"*/

import java.util.Scanner;

public class ej15 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		float num1, num2, num3;
		
		System.out.print("Introduce el primer número: ");
		num1 = teclado.nextFloat();
		System.out.print("Introduce el segundo número: ");
		num2 = teclado.nextFloat();
		System.out.print("Introduce el tercer número: ");
		num3 = teclado.nextFloat();
		
		if (num1 < 10 || num2 < 10 || num3 < 10 ) {
			System.out.println("Alguno de los números es menor a 10.");
		}
	}
}