package t11_4;

/*
Confeccionar un programa que permita introducir un valor del 1 al 10
y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si introduzco 3 deberá aparecer en pantalla los valores 3, 6, 9,
hasta el 36.
*/

import java.util.Scanner;

public class ej4 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int x, num;
		
		System.out.print("Introduce un número del 1 al 10: ");
		x = teclado.nextInt();
		
		for(int i = 1; i <= 10; i++) {
			num = x * i;
			
			System.out.println(x + " * " + i + " = " + num);
		}
	}
}
