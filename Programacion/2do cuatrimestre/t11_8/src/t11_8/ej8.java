package t11_8;

/*
Se cuenta con la siguiente información:
Las edades de 50 estudiantes del turno mañana.
Las edades de 60 estudiantes del turno tarde.
Las edades de 110 estudiantes del turno noche.
Las edades de cada estudiante deben introducirse por teclado.
	a) Obtener el promedio de las edades de cada turno (tres promedios)
	b) Imprimir dichos promedios (promedio de cada turno)
	c) Mostrar por pantalla un mensaje que indique cual de los tres turnos
	tiene un promedio de edades menor.
 */

import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class ej8 {
	public static void main(String[] args) {
		int sumaMa = 0, sumaTa = 0, sumaNo = 0;
		double promedioMa = 0, promedioTa = 0, promedioNo = 0;
		
		for(int i = 1; i <= 50; i++) {
			sumaMa += ThreadLocalRandom.current().nextInt(17, 100);
		}
		
		for(int i = 1; i <= 60; i++) {
			sumaTa += ThreadLocalRandom.current().nextInt(17, 100);
		}
		
		for(int i = 1; i <= 110; i++) {
			sumaNo += ThreadLocalRandom.current().nextInt(17, 100);
		}
		
		promedioMa = (double) sumaMa / 50;
		promedioTa = (double) sumaTa / 60;
		promedioNo = (double) sumaNo / 110;
		
		System.out.println("La edad promedio de la mañana es:" + promedioMa);
		System.out.println("La edad promedio de la tarde es:" + promedioTa);
		System.out.println("La edad promedio de la noche es:" + promedioNo);
	
		System.out.println("¿Cuál es el turno con menor edad?");
		if (promedioMa < promedioTa && promedioMa < promedioNo) System.out.println("El turno de mañana.");
		else if (promedioTa < promedioMa && promedioTa < promedioNo) System.out.println("El turno de tarde.");
		else System.out.println("El turno de noche.");
	}
}
