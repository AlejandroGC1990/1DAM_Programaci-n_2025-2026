package t10_1;

/*
Escribir un programa que solicite ingresar 10 notas de alumnos y
nos informe cuántos tienen notas mayores o iguales a 7 y cuántos
menores
*/

import java.util.Scanner;

public class ej1 {
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
        int x = 1, aprobados = 0, suspensos = 0;
        double nota;
        
        while (x <= 10) {
            System.out.print("Ingresa la nota del alumno numero " + x + ": ");
            nota = teclado.nextDouble();
            
            if (nota >= 7) {
                aprobados++;
            }
            else {
                suspensos++;
            }
            
            x++;
        }
        
        System.out.println("Cantidad de alumnos con notas mayores o iguales a 7 son: " + aprobados);
        System.out.println("Cantidad de alumnos con notas menores a 7 son: " + suspensos);
        
        teclado.close();
    }
}