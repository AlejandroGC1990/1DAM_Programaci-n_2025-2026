package ej18;

/*
Escribir un programa en el cual: dada una lista de tres valores numéricos
distintos se calcule e informe su rango de variación (debe mostrar el mayor y
el menor de ellos)
 * */

import java.util.Scanner;

public class ej18 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		double x, y, z, mayor, menor;
		
		System.out.print("Introduce el valor del primer número: ");
		x = teclado.nextDouble();
		System.out.print("Introduce el valor del segundo número: ");
		y = teclado.nextDouble();
		System.out.print("Introduce el valor del tercer número: ");
		z = teclado.nextDouble();
		
		/*MAYOR*/
		if (x > y && x > z) {
			mayor = x;
		}
		else if (y > x && y > z) {
			mayor = y;
		}
		else {
			mayor = z;
		}
		
		/*MENOR*/
		if (x < y && x < z) {
			menor = x;
		}
		else if (y < x && y < z) {
			menor = y;
		}
		else {
			menor = z;
		}
		
		System.out.println("El mayor es " + mayor);
		System.out.println("El menor es " + menor);
		
		teclado.close();
	}
}
