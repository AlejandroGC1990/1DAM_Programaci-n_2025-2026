/*
4. Se debe desarrollar un programa que pida el precio 
de un artículo y la cantidad que se lleva el cliente. 
Mostrar lo que debe abonar el comprador.
*/
import java.util.Scanner;

public class Ejercicio4 {

    public static void main(String[] ar) {
        Scanner teclado = new Scanner(System.in);
        float precio, precioFinal;
        int cantidad;

        System.out.print("Introduce el valor del producto: ");
        precio = teclado.nextFloat();
        System.out.print("Introduce la cantidad del producto que se lleva: ");
        cantidad = teclado.nextInt();

        precioFinal = precio * cantidad;

        System.out.print("La suma de la compra es: " + precioFinal);
    }
}