package t27_2;

import java.util.Scanner;

/*
 2. Cargar un String por teclado e implementar los siguientes métodos:
		a) Imprimir la primera mitad de los caracteres de la cadena.
		b) Imprimir el último carácter.
		c) Imprimirlo en forma inversa.
		d) Imprimir cada carácter del String separado con un guión.
		e) Imprimir la cantidad de vocales almacenadas.
		f) Implementar un método que verifique si la cadena se lee igual de izquierda a
		derecha tanto como de derecha a izquierda (ej. neuquen se lee igual en las dos
		direcciones)
 */

public class t27_2 {
    private Scanner teclado;
    private String cadena;

    public void cargar() {
        teclado = new Scanner(System.in);
        System.out.print("Ingrese una palabra o frase: ");
        cadena = teclado.nextLine();
    }

    // a) Imprimir la primera mitad
    public void primeraMitad() {
        String mitad = cadena.substring(0, cadena.length() / 2);
        System.out.println("Primera mitad: " + mitad);
    }

    // b) Imprimir el último carácter
    public void ultimoCaracter() {
        char ultimo = cadena.charAt(cadena.length() - 1);
        System.out.println("Último carácter: " + ultimo);
    }

    // c) Imprimir en forma inversa
    public void inversa() {
        System.out.print("Inversa: ");
        for (int i = cadena.length() - 1; i >= 0; i--) {
            System.out.print(cadena.charAt(i));
        }
        System.out.println();
    }

    // d) Separar con guiones
    public void separarPorGuion() {
        System.out.print("Separado por guiones: ");
        for (int f = 0; f < cadena.length(); f++) {
            System.out.print(cadena.charAt(f));
            if (f < cadena.length() - 1) {
                System.out.print("-");
            }
        }
        System.out.println();
    }

    // e) Cantidad de vocales
    public void cantidadVocales() {
        int cantidad = 0;
        String min = cadena.toLowerCase();
        for (int f = 0; f < min.length(); f++) {
            char letra = min.charAt(f);
            if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u') {
                cantidad++;
            }
        }
        System.out.println("Cantidad de vocales: " + cantidad);
    }

    // f) Verificar si es palíndromo
    public void esPalindromo() {
        int iguales = 0;
        int tam = cadena.length();
        for (int f = 0; f < tam / 2; f++) {
            if (cadena.charAt(f) == cadena.charAt(tam - 1 - f)) {
                iguales++;
            }
        }

        if (iguales == tam / 2) {
            System.out.println("Es palíndromo.");
        } else {
            System.out.println("No es palíndromo.");
        }
    }

    public static void main(String[] args) {
        t27_2 objeto = new t27_2();
        objeto.cargar();
        objeto.primeraMitad();
        objeto.ultimoCaracter();
        objeto.inversa();
        objeto.separarPorGuion();
        objeto.cantidadVocales();
        objeto.esPalindromo();
    }
}