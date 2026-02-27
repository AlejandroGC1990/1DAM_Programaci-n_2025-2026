package t27_3;

/*
Desarrollar un programa que solicite la carga de una clave. La clase debe 
tener dos métodos uno para la carga y otro que muestre si la clave es la 
correcta (la clave a comparar es "123abc")
*/

import java.util.Scanner;

public class t27_3 {
	private Scanner teclado;
	private String cadena;
	
	public void cargar() {
		teclado = new Scanner(System.in);
		System.out.print("Ingrese la clave: ");
		cadena = teclado.nextLine();
	}
	
	
	
}
