package t23_2;

import java.util.Scanner;

/*
  Crear una matriz de n * m filas (cargar n y m por teclado) Imprimir los
  cuatro valores que se encuentran en los vértices de la misma 
  (mat[0][0] etc.)
 */

public class t23_2 {
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
				System.out.print("Fila " + i + " Col " + j + ": ");
				mat[i][j] = teclado.nextInt();
			}
		}
	}
	
	public void imprimirVertices() {
		int ultCol = mat[0].length - 1;
		int ultFila = mat.length - 1;
		int ultColUltFila = mat[ultFila].length - 1;
		
		System.out.println("Superior Izquierdo [0][0]: " + mat[0][0]);
		System.out.println("Superior Derecho [0][" + ultCol + "]: " + mat[0][ultCol]);
		System.out.println("Inferior Izquierdo [" + ultFila + "][0]: " + mat[ultFila][0]);
		System.out.println("Inferior Derecho [" + ultFila + "][" + ultColUltFila + "]: " + mat[ultFila][ultColUltFila]);
	}
	
	public static void main(String[] args) {
        t23_2 ma = new t23_2();
        ma.cargar();
        ma.imprimirVertices();
    }
}
