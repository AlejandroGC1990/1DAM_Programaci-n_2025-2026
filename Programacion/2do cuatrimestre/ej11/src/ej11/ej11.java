package ej11;

/*Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente
 información: cantidad total de preguntas que se le realizaron y la cantidad de
 preguntas que contestó correctamente. Se pide confeccionar un programa que
 introduzca los dos datos por teclado y muestre el nivel del mismo según el
 porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
					Nivel máximo: Porcentaje>=90%.
					Nivel medio: Porcentaje>=75% y <90%.
					Nivel regular: Porcentaje>=50% y <75%.
					Fuera de nivel: Porcentaje<50%*/

import java.util.Scanner;

public class ej11 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int pregAprovadas, cantPreguntas, porcentaje;
		
		System.out.print("Introduce el número de preguntas realizadas: ");
		pregAprovadas = teclado.nextInt();
		System.out.print("Introduce la cantidad de preguntas totales: ");
		cantPreguntas = teclado.nextInt();
		
		porcentaje = (pregAprovadas * 100) / cantPreguntas;
		
		if (porcentaje >= 90) {
			System.out.println("Nivel máximo");
		}
		else if (porcentaje >= 75) {
			System.out.println("Nivel medio");
		}
		else if (porcentaje >= 50) {
			System.out.println("Nivel regular");
		}
		else {
			System.out.println("Fuera de nivel");
		}
	}
}
