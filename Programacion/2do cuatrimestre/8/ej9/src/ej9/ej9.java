package ej9;

/*Se introduce por teclado un valor entero, mostrar una leyenda que indique si el
 número es positivo, nulo o negativo.*/
 
import java.util.Scanner;

public class ej9 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int num;
		
		System.out.print("Introduce un valor: ");
		num = teclado.nextInt();
		
		if (num > 0) {
			System.out.println("El número es positivo.");
		}
		else {
			if (num < 0) {
				System.out.println("El número es negativo.");				
			}
			else {
				System.out.println("El número es nulo.");
			}
		}
		
	}
}
