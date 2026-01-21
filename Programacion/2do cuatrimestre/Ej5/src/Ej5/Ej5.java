/*Se introducen tres notas de un alumno, si el promedio es 
 * mayor o igual a siete mostrar un mensaje "Promocionado".*/

package Ej5;

import java.util.Scanner;

public class Ej5 {
	public static void main(String [] ar) {
		Scanner teclado = new Scanner(System.in);
		float num1, num2, num3, promedio;
		
		System.out.println("Primera nota: ");
		num1 = teclado.nextInt();
		System.out.println("Segundaa nota: ");
		num2 = teclado.nextInt();
		System.out.println("Tercera nota: ");
		num3 = teclado.nextInt();
		
		promedio = (num1 + num2 + num3)/3;
		
		if (promedio >= 7) {
			System.out.println("Promociona");
		}
		
		System.out.println("El promedio final es: " + promedio);
	
		teclado.close();
	}
}
