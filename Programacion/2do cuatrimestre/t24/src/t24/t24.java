package t24;

/*
Se desea saber la temperatura media trimestral de cuatro países. Para ello 
se tiene como dato las temperaturas medias mensuales de dichos países. Se
debe introducir el nombre del país y seguidamente las tres temperaturas 
medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de 
los datos en memoria.
	a - Cargar por teclado los nombres de los países y las temperaturas 
	medias mensuales.
	b - Imprimir los nombres de las países y las temperaturas medias 
	mensuales de las mismas.
	c - Calcular la temperatura media trimestral de cada país.
	d - Imprimir los nombres de los países y las temperaturas medias 
	trimestrales.
	e - Imprimir el nombre del país con la temperatura media trimestral 
	mayor.
 */

import java.util.Scanner;

public class t24 {
	private Scanner teclado;
	private String[] paises;
	private int[][] tempMediasMensuales;
	private float[] tempMediasTrimestrales;
	
	public void cargar() {
		teclado = new Scanner(System.in);
		paises = new String[4];
		tempMediasMensuales = new int[4][3];
		
		for(int i = 0; i < paises.length; i++) {
			System.out.print("Introduce el nombre del país: ");
			paises[i] = teclado.next();
			
			for(int j = 0; j < tempMediasMensuales[i].length; j++) {
				System.out.print("Introduce la temperatura del mes " + (j + 1) + ": ");
				tempMediasMensuales[i][j] = teclado.nextInt();
			}
		}
	}
	
	public void imprimirPaisesTemperaturasM() {
		System.out.println("Paises y Temperaturas: ");
		for(int k = 0; k < paises.length; k++) {
			System.out.print(paises[k] + ": ");
		
			for(int j = 0; j < tempMediasMensuales[k].length; j++) {
                System.out.print(tempMediasMensuales[k][j] + "ºC ");
            }
            
			System.out.println();
        }
	}
	
	public void calcularTemperaturasTrimestrales() {
		tempMediasTrimestrales = new float[paises.length];
		
		for(int l = 0; l < tempMediasMensuales.length; l++) {
			float suma = 0;
			for(int m = 0; m < tempMediasMensuales[l].length; m++) {
				suma = suma + tempMediasMensuales[l][m];
			}
			
			tempMediasTrimestrales[l] = suma / 3;
		}
	}
	
	public void imprimirTemperaturasTrimestrales() {
		System.out.println("Temperaturas medias trimestrales: ");
		for(int n = 0; n < tempMediasTrimestrales.length; n++) {
			System.out.println(paises[n] + " - " + tempMediasTrimestrales[n] + " ºC");
		}
	}
	
	public void paisMayorTemp() {
		float mayor = tempMediasTrimestrales[0];
		String nombreMayor = paises[0];
		
		for(int p = 0; p < tempMediasTrimestrales.length; p++) {
			if(tempMediasTrimestrales[p] > mayor) {
				mayor = tempMediasTrimestrales[p];
				nombreMayor = paises[p];
			}
		}
		System.out.println("El país con mayor temperatura media trimestral es " + nombreMayor + " con " + mayor + "ºC");
	}
	
	public static void main(String[] ar) {
		t24 ma = new t24();
		ma.cargar();
		ma.imprimirPaisesTemperaturasM();
		ma.calcularTemperaturasTrimestrales();
        ma.imprimirTemperaturasTrimestrales();
        ma.paisMayorTemp();
	}
}
