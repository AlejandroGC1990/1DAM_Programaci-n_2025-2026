package Ej1;

/*Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro
del mismo (El perímetro de un cuadrado se calcula multiplicando el valor del
lado por cuatro)*/

import java.util.Scanner;

public class Ej1 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int lado, perimetro;
		
		System.out.print("Ingrese el lado del cuadrado: ");
        lado = teclado.nextInt();
        
        perimetro = lado * 4;
        
        System.out.println("El perimetro del cuadrado es: " + perimetro);
	}
}
