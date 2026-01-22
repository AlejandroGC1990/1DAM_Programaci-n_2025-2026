package ej7;

/*Se introducen por teclado un número positivo de uno o dos dígitos (1..99)
mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos, un
número entero).*/

import java.util.Scanner;

public class ej7 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int num;
		
		if (num >= 10) {
			System.out.println("El número tiene 2 díjitos.")
		}
		else {
			System.out.println("El número tiene 1 díjito.")			
		}
	}
}
