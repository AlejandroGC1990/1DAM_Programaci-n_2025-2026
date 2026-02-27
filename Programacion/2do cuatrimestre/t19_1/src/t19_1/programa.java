package t19_1;

/*
 Cargar un vector de n elementos. imprimir el menor y un mensaje si se 
 repite dentro del vector.
 */

import java.util.Scanner;

public class programa {
	private Scanner teclado;
	private float[] vector;
	private int n;
	
	public void cargar() {
		teclado = new Scanner(System.in);
		System.out.println("¿CUántos elementos tendrá el vector? ");
		n = teclado.nextInt();
		vector = new float[n];
		
		for(int i = 0; i < n; i++) {
			System.out.println("Ingrese elemento " + (i + 1) + ": ");
			vector[i] = teclado.nextFloat();
		}
	}
	
	public void buscarMenor() {
		float menor = vector[0];
		for (int i = 0; i < vector.length; i++) {
			if(vector[i] < menor) {
				menor = vector[i];
			}
		}
		System.out.println();
	}
}
