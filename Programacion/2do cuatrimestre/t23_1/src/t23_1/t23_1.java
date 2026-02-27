package t23_1;

/*
  Crear una matriz de n * m filas (cargar n y m por teclado) Intercambiar
  la primer fila con la segunda. Imprimir luego la matriz 
 */

import java.util.Scanner;

public class t23_1 {
	private Scanner teclado;
	private int[][] mat;
	
	public void cargar() {
		teclado = new Scanner(System.in);
		System.out.print("Cuantas filas tiene la matriz: ");
		int filas = teclado.nextInt();
		System .out.print("Cuantas columnas tiene la matriz: ");
		int columnas = teclado.nextInt();
		
		mat = new int[filas][columnas];
		
		for(int i = 0; i < mat.length; i++) {
			for(int j = 0; j < mat[i].length; j++) {
				System.out.print("Introduce componente: ");
				mat[i][j] = teclado.nextInt();
			}
		}
	}
	
	public void intercambiar() {
		for(int i = 0; i < mat[0].length; i++) {
			int aux = mat[0][i];
			mat[0][i] = mat[1][i];
			mat[1][i] = aux;
		}
	}
		
	public void imprimir() {
		for(int i = 0; i<mat.length; i++) {
			for(int j = 0; j<mat[i].length; j++) {
				System.out.print(mat[i][j] + " ");
			}
			System.out.println(" ");
		}
	}
	
	public static void main(String[] args) {
        t23_1 matriz = new t23_1();
        matriz.cargar();
        matriz.intercambiar();
        matriz.imprimir();
    }
	
}
