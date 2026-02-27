package t11_6;

/*
Escribir un programa que pida ingresar coordenadas (x,y) que representan
puntos en el plano.
	a)Informar de cuántos puntos se han introducido en el primer, segundo,
	tercer y cuarto cuadrante. Al comenzar el programa se pide que se 
	introduzca la cantidad de puntos a procesar.
*/

import java.util.Scanner;

public class ej6 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int n = 0, c1 = 0, c2 = 0, c3 = 0, c4 = 0;
		double x, y;
		
		System.out.println("Introduce el número de pares de coordenadas a procesar: ");
		n = teclado.nextInt();
		
		for (int i = 1; i <= n; i++) {
			System.out.println("Introduce la coordenada X: ");
			x = teclado.nextDouble();
			System.out.println("Introduce la coordenada Y: ");
			y = teclado.nextDouble();
			
			if(x > 0 && y > 0) c1++;
			else if(x < 0 && y > 0) c2++;
			else if(x < 0 && y < 0) c3++;
			else if(x > 0 && y < 0) c4++;				
		}
		
		System.out.println("\n--- RESULTADOS ---");
        System.out.println("Puntos en el 1º cuadrante: " + c1);
        System.out.println("Puntos en el 2º cuadrante: " + c2);
        System.out.println("Puntos en el 3º cuadrante: " + c3);
        System.out.println("Puntos en el 4º cuadrante: " + c4);

        teclado.close();
	}
}
