package t11_2;

/*Desarrollar un programa que solicite la carga de 10 números e 
imprima la suma de los últimos 5 valores introducidos.*/

import java.util.Scanner;

public class ej2 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int i;
		double num, suma = 0;
		
		for (i = 1; i <= 10; i++) {
			System.out.print("Introduce un número: ");
			num = teclado.nextDouble();
			
			if (i > 5) suma += num;
		}
		
		System.out.println("La suma de los últimos 5 valores es: " + suma +".");
	}
}
