package t26_2;

/*
Implementar la clase operaciones. Se deben cargar dos valores enteros en 
el constructor, calcular su suma, resta, multiplicación y división, cada
una en un método, imprimir dichos resultados.
 */

import java.util.Scanner;

public class Operaciones {
	private Scanner teclado;
	private int valor1;
	private int valor2;
	
	//Constructor: Carga los valores iniciales
	public Operaciones() {
		teclado = new Scanner(System.in);
		System.out.println("Ingrese el primer valor: ");
		valor1 = teclado.nextInt();
		System.out.println("Ingrese el segundo valor: ");
		valor2 = teclado.nextInt();
	}
	
	//Método para sumar.
	public void sumar() {
		int suma = valor1 + valor2;
		System.out.println("La suma es: " + suma);
	}
	
	//Método para restar.
	public void restar() {
		int resta = valor1 - valor2;
		System.out.println("La resta es: " + resta);
	}
	
	//Método para multiplicar.
	public void multiplicar() {
		int multiplicar = valor1 * valor2;
		System.out.println("La multiplicación es: " + multiplicar);
	}
	
	//Método para dividir.
	public void dividir() {
		float dividir = valor1 / valor2;
		System.out.println("La dividisión es: " + dividir);
	}
	
	public static void main(String[] ar) {
        // Creo el objeto, lo que dispara automáticamente el constructor (carga de datos)
        Operaciones op = new Operaciones();
        // Llamo a cada método para realizar los cálculos e imprimir
        op.sumar();
        op.restar();
        op.multiplicar();
        op.dividir();
    }
}
