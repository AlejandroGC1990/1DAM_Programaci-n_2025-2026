import javax.swing.*;

public class ej1 extends JFrame {
	private JLabel label1, label2, label3;
	public ej1() {
		setLayout(null);
		label1 = new JLabel("Patata");
		label1.setBounds(10,20,300,30);
		add(label1);
		label2 = new JLabel("Patata brava");
		label2.setBounds(10,40,300,30);
		add(label2);
		label3 = new JLabel("Patata alioli");
		label3.setBounds(10,60,300,30);
		add(label3);
	}
	
	public static void main(String[] ar) {
		ej1 ventana = new ej1();
		ventana.setBounds(0,0,400,200);
		ventana.setResizable(false);
		ventana.setVisible(true);
		ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
