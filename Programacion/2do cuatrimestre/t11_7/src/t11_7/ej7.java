package t11_7;

/*
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
	a) La cantidad de valores introducidos negativos.
	b) La cantidad de valores introducidos positivos.
	c) La cantidad de múltiplos de 15.
	d) El valor acumulado de los números ingresados que son pares.
*/

import java.util.Scanner;

public class ej7 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int x = 10, negativos = 0, positivos = 0, mult15 = 0, num, pares = 0;
		
		for(int i = 1; i <= 10; i++) {
			System.out.println("("+ i +")Inserte un número entero (positivo o negativo): ");
			num = teclado.nextInt();
			
			if (num < 0) negativos++;
			else if (num >= 0) positivos++;
			
			if (num % 15 == 0) mult15++;
			if (num % 2 == 0) pares += num;			
		}
		
		System.out.println("La cantidad de números positivos introducidos es: " + positivos);
		System.out.println("La cantidad de números negativos introducidos es: " + negativos);
		System.out.println("La cantidad de números múltiplos de 15 introducidos es: " + multi15);
		System.out.println("La cantidad sumada de los números pares introducidos es: " + pares);
	}
}
