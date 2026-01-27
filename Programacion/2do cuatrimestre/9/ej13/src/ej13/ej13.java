package ej13;

/*Se introducen tres valores por teclado, si todos son iguales se imprime la suma
del primero con el segundo y a este resultado se lo multiplica por el tercero.*/

import java.util.Scanner;

public class ej13 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		float num1, num2, num3, suma, producto;
		
		System.out.print("Introduce el primer valor: ");
		num1 = teclado.nextFloat();
		System.out.print("Introduce el segundo valor: ");
		num2 = teclado.nextFloat();
		System.out.print("Introduce el tercer valor: ");
		num3 = teclado.nextFloat();
		
		if (num1 == num2 && num1 == num3) {
			suma = num1 + num2;
			producto = suma * num3;
			
			System.out.println("Todos los números son iguales y la suma de los 2 primeros números da " + suma + " , mientras el producto con el tercero da " + producto + ".");
		}
	}
}
