package ej17;

/*
 De un operario se conoce su sueldo y los años de antigüedad. Se pide
 confeccionar un programa que lea los datos de entrada e informe:
	 a) Si el sueldo es inferior a 500 y su antigüedad es igual o 
	 superior a 10 años, otorgarle un aumento del 20 %, mostrar el 
	 sueldo a pagar.
	 b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 
	 10 años, otorgarle un aumento de 5 %.
	 c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla 
	 sin cambios.
 */

import java.util.Scanner;

public class ej17 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int anos;
		float sueldo;
		
		System.out.print("Introduce el sueldo del trabajador: ");
		sueldo = teclado.nextFloat();
		System.out.print("Introduce el número de años que ha trabajado el empleado: ");
		anos = teclado.nextInt();
		
		if (sueldo < 500 && anos >= 10) {
			sueldo *= 1.20f;
			System.out.println("El sueldo se ha subido un 20% y ahora es: " + sueldo);
		}
		else if (sueldo < 500 && anos < 10) {
			sueldo *= 1.05f;
			System.out.println("El sueldo se ha subido un 5% y ahora es: " + sueldo);
		}
		else {
			System.out.println("El sueldo es: " + sueldo);
		}
		
		teclado.close();
	}	
}
