package t18_1;

/*
Desarrollar un programa que permita cargar 5 nombres de personas y sus 
edades respectivas. Después de realizar la carga por teclado de todos los
datos imprimir los nombres de las personas mayores de edad (mayores o 
iguales a 18 años).
*/

import java.util.Scanner;

public class t18_1 {
	private Scanner teclado;
	private String[] nombres;
	private int[] edades;
	
	public void cargar() {
		teclado = new Scanner(System.in);
		nombres = new String[5];
		edades = new int[5];
		
		for(int i = 0; i < 5; i++) {
			System.out.println("Introduce el nombre " + (i + 1) + " : ");
			nombres[i] = teclado.next();
			System.out.println("Introduce la edad " + (i + 1) + " : ");
			edades[i] = teclado.nextInt();
		}
	}
	
	public void mayoresEdad() {
		System.out.println("Personas mayores de edad: ");
			for(int i = 0; i < nombres.length; i++) {
				if(edades[i] >= 18) {
					System.out.println(nombres[i]);
				}
			}
	}

	public static void main(String[] ar) {
		t18_1 p = new t18_1();
		p.cargar();
		p.mayoresEdad();
	}
	
}
