package t11_5;

/*
Realizar un programa que lea los lados de n triángulos, e informar:
	a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres 
	lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado
	igual).
	b) Cantidad de triángulos de cada tipo.
	c) Tipo de triángulo que posee menor cantidad.
 */

import java.util.Scanner;

public class ej5 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int nt = 0, escaleno = 0, isosceles = 0, equilatero = 0;
		double lado1, lado2, lado3;
		
		System.out.print("Introduce el número de triángulos a contar: ");
		nt = teclado.nextInt();
		
		for(int i = 1; i <= nt; i++) {
			System.out.println("Introduce el valor del lado 1 en cm: ");
			lado1 = teclado.nextDouble();
			System.out.println("Introduce el valor del lado 2 en cm: ");
			lado2 = teclado.nextDouble();
			System.out.println("Introduce el valor del lado 3 en cm: ");
			lado3 = teclado.nextDouble();
			
			if(lado1 == lado2 && lado1 == lado3) {
				System.out.println("El triángulo " + i + " es equilátero");
				equilatero++;
			}
			else if(lado1 == lado2 || lado1 == lado3 || lado2 == lado3) {
				System.out.println("El triángulo " + i + " es isósceles");
				isosceles++;
			}
			else {
				System.out.println("El triángulo " + i + " es escaleno");
				escaleno++;
			}
		}
		
		System.out.println("\n--- RESUMEN FINAL ---");
		System.out.println(equilatero + "triángulo/s equilátero/s.");
		System.out.println(isosceles + "triángulo/s isosceles.");
		System.out.println(escaleno + "triángulo/s escaleno/s.");
		
		if(escaleno < isosceles && escaleno < equilatero) System.out.println("El grupo de menos triángulos es escaleno con " + escaleno + " triángulos");
		else if(isosceles < escaleno && isosceles < equilatero) System.out.println("El grupo de menos triángulos es isósceles con " + isosceles + " triángulos");
		else System.out.println("El grupo de menos triángulos es equilátero con " + equilatero + " triángulos");
	}
}