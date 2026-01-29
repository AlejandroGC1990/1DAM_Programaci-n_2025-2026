package t11_1;

/*
Confeccionar un programa que lea n pares de datos, cada par de datos
corresponde a la medida de la base y la altura de un triángulo. El 
programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su 
superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12
*/

import java.util.Scanner;

public class ej1 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int n, mayor12 = 0, x = 1;
		double superficie, base, altura;
		
		System.out.print("Ingresa el número  de triángulos: ");
		n = teclado.nextInt();
		
		while (x <= n) {
			System.out.print("Ingresa la altura del triángulo: ");
			altura = teclado.nextDouble();
			System.out.print("Ingresa la base del triángulo: ");
			base = teclado.nextDouble();
		
			superficie = (base * altura)/2;
			
			if (superficie > 12) mayor12++;
			
			System.out.println("Las medidas del triángulo nº " + x + " es " + altura + "cm de altura y " + base + "cm de base.");
			
			x++;
		}
		
		System.out.print("Hay " + mayor12 + " triángulos con una superficie mayor a 12");
		
		teclado.close();
	}
}
