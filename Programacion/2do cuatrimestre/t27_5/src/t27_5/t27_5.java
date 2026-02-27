package t27_5;

import java.util.Scanner;

/* 	Codifique un programa que permita cargar una oración por teclado, luego
	mostrar cada palabra introducida en una línea distinta.
	 Por ejemplo si cargo: La mañana está fría.
	 Debe aparecer:
		 La
		 mañana
		 está
		 fría.
 */

import java.util.scaner;

public class t27_5 {
	private Scanner teclado;
    private String oracion;

    public void cargar() {
        teclado = new Scanner(System.in);
        System.out.print("Ingrese una oración: ");
        oracion = teclado.nextLine();
    }

    public void mostrarPalabras() {
        System.out.println("\nPalabras desglosadas:");

        for (int f = 0; f < oracion.length(); f++) {
            if (oracion.charAt(f) != ' ') {
                System.out.print(oracion.charAt(f));
            } 
            else {
                System.out.println();
            }
        }
        
        System.out.println();
    }

    public static void main(String[] args) {
        t27_5 programa = new t27_5();
        programa.cargar();
        programa.mostrarPalabras();
    }
}