package ej12;

/*Realizar un programa que pida cargar una fecha cualquiera, luego verificar si
dicha fecha corresponde a Navidad*/

import java.util.Scanner;

public class ej12 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int dia, mes;
		
		System.out.print("Introduce el día del mes: ");
		dia = teclado.nextInt();
		System.out.print("Introduce el número de mes: ");
		mes = teclado.nextInt();
		
		if (dia == 25 && mes == 12) {
			System.out.println("SI! ES NAVIDAD!!");
		}
		else {
			System.out.println("No es Navidad");
		}
	}
}
