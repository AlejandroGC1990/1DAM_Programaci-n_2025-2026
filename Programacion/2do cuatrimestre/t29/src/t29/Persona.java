package t29;

/*
 Confeccionar una clase Persona que tenga como atributos el nombre y la
edad. Definir como responsabilidades un método que cargue los datos
personales y otro que los imprima.
 Plantear una segunda clase Empleado que herede de la clase Persona.
 Añadir un atributo sueldo y los métodos de cargar el sueldo e imprimir su
 sueldo.
 Definir un objeto de la clase Persona y llamar a sus métodos. También
 crear un objeto de la clase Empleado y llamar a sus mét
 */

import java.util.Scanner;

public class Persona {
    protected Scanner teclado; 
    protected String nombre;
    protected int edad;

    public void cargarDatosPersonales() {
        teclado = new Scanner(System.in); 
        System.out.print("Ingrese nombre: ");
        nombre = teclado.next();
        System.out.print("Ingrese edad: ");
        edad = teclado.nextInt();
    }
    
    public void imprimirDatosPersonales() {
    	System.out.println("Nombre: " + nombre);
    	System.out.println("Edad: " + edad);
    }
}
