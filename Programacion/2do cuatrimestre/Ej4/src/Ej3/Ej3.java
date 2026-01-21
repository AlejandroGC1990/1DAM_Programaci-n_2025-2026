package Ej3;
/*Realizar un programa que lea por teclado dos números, si el
 * primero es mayor al segundo mostrar su suma y diferencia, 
 * en caso contrario mostrar el producto y la división del 
 * primero respecto al segundo. * */

import java.util.Scanner;

public class Ej3 {

		public static void main(String[] ar) {
			Scanner teclado = new Scanner(System.in);
			float num1, num2;
			
			System.out.print("Primer número: ");
			num1 = teclado.nextFloat();
			System.out.print("Segundo número: ");
			num2 = teclado.nextFloat();
			
			if (num1 > num2) {
				float suma = num1 + num2;
				float diferencia = num1 - num2;
				System.out.print("Suma: " + suma);
				System.out.print("Resta: " + diferencia);
			}
			else {
				float producto = num1 * num2;
				float division = num1 / num2;
				System.out.print("Producto: " + producto);
				System.out.print("División: " + division);
			}
			teclado.close();
		}
}
