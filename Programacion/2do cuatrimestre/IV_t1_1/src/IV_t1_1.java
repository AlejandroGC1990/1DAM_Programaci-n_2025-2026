/*
Crear una ventana de 1024 píxeles por 800 píxeles. Luego no 
permitir que el operador modifique el tamaño de la ventana. 
Sabiendo que hacemos visible al JFrame llamando el método 
setVisible pasando el valor true, existe otro método llamado 
setResizable que también requiere como parámetro un valor true 
o false.
*/

import javax.swing.JFrame;

public class IV_t1_1 extends JFrame {
	
	public IV_t1_1() {
		 setLayout(null);
		 setBounds(0, 0, 1024, 800);
		 setResizable(false);
		 setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public static void main(String[] ar) {
		IV_t1_1 ventana1 = new IV_t1_1();
		ventana1.setVisible(true);
	}
}
