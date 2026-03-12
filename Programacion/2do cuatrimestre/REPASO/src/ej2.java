/*
 Este programa solicitará al usuario introducir una frase, luego 
 imprimirá la frase original y realizará las siguientes operaciones 
 con la frase:
  1.Contar el número de carácteres en frase.
  2.Contar el número de palabras en la frase.
  3.Invertir la frase (utiliza el método reverse()).
  4.Verificar si la frase es un palíndromo. 
 */

import java.util.Scanner;

public class ej2 {
	private Scanner teclado;
	private String frase;
	
	public void cargar() {
		teclado = new Scanner(System.in);
		System.out.println("Ingrese una frase: ");
		frase = teclado.nextLine(); 
	}
	
	//Contar número de carácteres en frase
	public void contarCaractreres() {
		int caracteres = 0;
		System.out.println("\n Número de caráctreres: ");
		for (int i = 0; i < frase.length(); i++) {
			if (frase.charAt(i) != ' ') {
				caracteres++;
			}
		}
		System.out.println("El número de carácteres (sin contar espacios) es " + caracteres);
	}
	
	//Contar palabras de la frase
	public void contarPalabras() {
		int palabras = 0;
		System.out.println("\n Número de palabras: ");
		for (int i = 0; i < frase.length(); i++) {
			if (frase.charAt(i) == ' ') {
				palabras++;
			}
		}
		System.out.println("El número de carácteres (sin contar espacios) es " + palabras);
	}
	
	//Darle la vuelta a la frase
}
