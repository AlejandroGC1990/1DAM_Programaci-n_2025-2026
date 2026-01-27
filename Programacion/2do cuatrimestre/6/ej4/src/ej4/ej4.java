package ej4;

/*Se debe desarrollar un programa que pida el precio de un artículo y la
cantidad que se lleva el cliente. Mostrar lo que debe abonar el comprador.*/

import java.util.Scanner;

public class ej4 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		float precio;
		int cantidad;
		float total;
		
		System.out.print("Ingrese el precio del artículo: ");
		precio = teclado.nextFloat();
		System.out.print("Ingrese la cantidad de artículos: ");
		cantidad = teclado.nextInt();
		
		total = precio * cantidad;
		
		System.out.println("El total a abonar es: " + total);
	}
}
