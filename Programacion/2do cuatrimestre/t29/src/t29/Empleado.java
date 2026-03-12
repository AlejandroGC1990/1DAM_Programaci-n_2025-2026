package t29;

public class Empleado extends Persona{
	private float sueldo;
	
	public void cargarSueldo() {
		System.out.print("Ingrese el sueldo de " + nombre + ": ");
		sueldo = teclado.nextFloat();
	}
	
	public void imprimirSueldo() {
		System.out.println("Sueldo: " + sueldo);
	}
}
