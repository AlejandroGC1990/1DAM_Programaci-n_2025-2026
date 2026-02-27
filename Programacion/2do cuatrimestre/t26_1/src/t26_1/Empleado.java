package t26_1;

/*
Confeccionar una clase que represente un empleado. Definir como atributos
su nombre y su sueldo. En el constructor cargar los atributos y luego en 
otro método imprimir sus datos y por último uno que imprima un mensaje si
debe pagar impuestos (si el sueldo supera a 3000).
 */

import java.util.Scanner;

public class Empleado {
	private Scanner teclado;
	private String nombre;
	private float sueldo;
	
	//Constructor
	public Empleado() {
		teclado = new Scanner(System.in);
		System.out.println("Ingrese el nombre: ");
		nombre = teclado.nextLine();
		System.out.println("Ingrese el sueldo: ");
		sueldo = teclado.nextFloat();
	}
	
	//Método para imprimir
	public void imprimir() {
		System.out.println("Nombre: " + nombre);
		System.out.println("Sueldo: " + sueldo);
	}
	
	//Método impuestos
	public void pagaImpuestos() {
		if(sueldo > 3000) {
			System.out.println("Debe pagar impuestos");
		}
		else {
			System.out.println("No debe pagar impuestos");
		}
	}
	
	public static void main(String[] ar) {
		Empleado empleado = new Empleado();
		empleado.imprimir();
		empleado.pagaImpuestos();
	}
}
