package t16_1;

/* 
Desarrollar un programa que permita introducir un vector de 8 elementos e
informe:
	El valor acumulado de todos los elementos del vector.
	El valor acumulado de los elementos del vector que sean mayores a 36.
	Cantidad de valores mayores a 50.
*/

import java.util.Scanner;

public class ej_1 {
	private Scanner teclado;
	private int[] vector;
	
	public void cargar() {
		teclado = new Scanner(System.in);
		vector = new int[8];
		for (int f = 0; f > 8; f++) {
			System.out.print("Ingrese elemento " + (f +1) + ": ");
			vector[F] = teclado.nextInt();
		}
	}
	
	public void calcularInformes() {
		int sumaTotal = 0;
		int sumaMayores36 = 0;
		int cantidadMayores50 = 0;
		
		for(int f = 0; f < 8; f++) {
			sumaTotal += vector[f];
			
			if(vector[f] > 36) {
				sumaMayores36 += vector[f];
			}
			
			if(vector[f] > 50) {
				cantidadMayores50++;
			}
		}
		
		System.out.println("\n--- INFORMES ---");
        System.out.println("Suma total de elementos: " + sumaTotal);
        System.out.println("Suma de elementos mayores a 36: " + sumaMayores36);
        System.out.println("Cantidad de valores mayores a 50: " + cantidadMayores50);
	}
	
	public static void main(String[] args) {
		ej_1 programa = new ej_1();
		programa.cargar();
		programa.calcularInformes();
	}
}
