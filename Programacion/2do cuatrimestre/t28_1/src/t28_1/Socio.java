package t28_1;

import java.util.Scanner;

public class Socio {
	private String nombre;
	private int antiguedad;
	
	public Socio() {
		Scanner teclado = new Scanner(System.in);
		System.out.print("Ingrese el nomnbre del socio");
		nombre = teclado.next();
		System.out.print("Ingrese la antigüedad (en años): ");
		antiguedad = teclado.nextInt();
	}
	
	public void imprimir() {
		System.out.println(nombre + " tiene una antigüedad de " + antiguedad + "años.");
	}
	
	public int retornarAntiguedad() {
		return antiguedad;
	}
	
	public String retornarNombre() {
		return nombre;
	}
}
