package t11_3;

/*
Desarrollar un programa que muestre la tabla de multiplicar del 5 
(del 5 al 50)
*/

import java.util.Scanner;

public class ej3 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int num;
		
		for(int i = 1; i <=10; i++) {
			num = 5 * i;
			System.out.println("5 x " + i + " = " + num);
		}
	}
}
