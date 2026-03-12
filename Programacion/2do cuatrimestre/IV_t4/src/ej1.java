import javax.swing.*;
import java.awt.event.*;

public class ej1 extends JFrame implements ActionListener {
    private JTextField tfUsuario, tfClave;
    private JLabel label1, label2;
    private JButton botonVerificar;

    public ej1() {
        setLayout(null);
        
        label1 = new JLabel("Usuario:");
        label1.setBounds(10, 10, 100, 30);
        add(label1);
        
        tfUsuario = new JTextField();
        tfUsuario.setBounds(120, 10, 150, 30);
        add(tfUsuario);

        label2 = new JLabel("Clave:");
        label2.setBounds(10, 50, 100, 30);
        add(label2);
        
        tfClave = new JTextField();
        tfClave.setBounds(120, 50, 150, 30);
        add(tfClave);

        botonVerificar = new JButton("Ingresar");
        botonVerificar.setBounds(10, 90, 100, 30);
        add(botonVerificar);
        botonVerificar.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == botonVerificar) {
            String user = tfUsuario.getText();
            String pass = tfClave.getText();

            if (user.equals("juan") && pass.equals("abc123")) {
                setTitle("Correcto");
            } else {
                setTitle("Incorrecto");
            }
        }
    }

    public static void main(String[] args) {
        ej1 ventana = new ej1();
        ventana.setBounds(0, 0, 300, 180);
        ventana.setVisible(true);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}