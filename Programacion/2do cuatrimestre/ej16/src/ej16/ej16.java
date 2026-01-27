package ej16;

/*Escribir un programa que pida introducir la coordenada de un punto en el plano,
es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º
Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)*/

import java.util.Scanner;

public class ej16 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int x, y;
		
		System.out.print("Introduce las coordenadas X: ");
		x = teclado.nextInt();
		System.out.print("Introduce las coordenadas Y: ");
		y = teclado.nextInt();
		
		if (x >= 0 && y >= 0) {
			System.out.println("Las coordenadas son del cuadrante 1.");
		}
		else if (x > 0 && y < 0) {
			System.out.println("Las coordenadas son del cuadrante 2.");
		}
		else if (x < 0 && y < 0) {
			System.out.println("Las coordenadas son del cuadrante 3.");
		}
		else if (x < 0 && y > 0) {
			System.out.println("Las coordenadas son del cuadrante 4.");
		}
		else {
			System.out.println("El punto se encuentra sobre uno de los ejes.");
		}
	}
}
