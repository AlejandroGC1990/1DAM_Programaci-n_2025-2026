/*
 -Este programa solicitará al usuario que introduzca el número de filas y
 columnas de una matriz.
 -Luego pedirá al usuario que introduzca los elementos de la matriz. 
 -Luego, imprimirá la matriz original, calculará la suma de todos los elementos 
 de la matriz y la suma de cada fila de la matriz, y finalmente
 mostrará los resultados.
 */

import java.util.Scanner;

public class ej1 {
	private Scanner teclado;
	private int[][] matriz;
	private int filas, columnas;
	
	public void cargar() {
		teclado = new Scanner(System.in);
		System.out.print("Ingrese el número de filas: ");
		filas = teclado.nextInt();
		
		System.out.print("Ingrese el número de columnas: ");
		columnas = teclado.nextInt();
		
		//Se crea la matriz
		matriz = new int[filas][columnas];
		
		//Cargar los elementos
		for(int i = 0; i < filas; i++) {
			for(int j = 0; j < columnas; j++) {
				System.out.print("Ingrese el elemento [" + i + "][" + j + "]: ");
				matriz[i][j] = teclado.nextInt();
			}
		}
	}	
	
	public void mostrarYCalcular() {
		int sumaTotal = 0;
		System.out.println("\n Matriz Original y suma de filas: ");
		
		for(int f = 0; f < filas; f++) {
			int sumaFila = 0;
			for(int c = 0; c < matriz[f].length; c++) {
				System.out.println(matriz[f][c] + " ");
				sumaTotal += matriz[f][c];
				sumaFila += matriz[f][c];
			}
			System.out.println("| Suma fila: " + sumaFila);
		}
		System.out.println("\n La suma de todos los elementos es: " + sumaTotal);
	}
			
	public static void main(String[] ar) {
		ej1 matriz = new ej1();
		matriz.cargar();
		matriz.mostrarYCalcular();
	}
}
