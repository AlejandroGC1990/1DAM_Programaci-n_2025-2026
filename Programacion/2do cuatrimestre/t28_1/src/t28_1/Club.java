package t28_1;

public class Club {
	private Socio socio1, socio2, socio3;
	
	public Club() {
		System.out.println("Carga del Socio 1: ");
		socio1 = new Socio();
		System.out.println("Carga del Socio 2:");
		socio2 = new Socio();
		System.out.println("Carga del Socio 3:");
		socio3 = new Socio();
	}
	
	public void mayorAntigüedad() {
		System.out.print("El socio con mnayor antigüedad es: ");
		
		if (socio1.retornarAntiguedad() > socio2.retornarAntiguedad() &&
			socio1.retornarAntiguedad() > socio3.retornarAntiguedad()) {
			System.out.println(socio1.retornarNombre());
		} else {
			if (socio2.retornarAntiguedad() > socio3.retornarAntiguedad()) {
				System.out.println(socio2.retornarNombre());
			} else {
				System.out.println(socio3.retornarNombre());
			}
		}
	}
	
	public static void main(String[] ar) {
		Club club1 = new Club();
		club1.mayorAntigüedad();
	}
}
