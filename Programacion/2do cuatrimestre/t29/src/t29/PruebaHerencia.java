package t29;

public class PruebaHerencia {
	public static void main(String[] args) {
		Persona persona1 = new Persona();
		persona1.cargarDatosPersonales();
		persona1.imprimirDatosPersonales();
		
		Empleado empleado1 = new Empleado();
		empleado1.cargarDatosPersonales();
		empleado1.cargarSueldo();
		
		System.out.println("Resultados del empleado");
		empleado1.imprimirDatosPersonales();
		empleado1.imprimirSueldo();
	}
}
