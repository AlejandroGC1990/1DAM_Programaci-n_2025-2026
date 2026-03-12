import javax.swing.*;
import java.awt.event.*;

public class Ej1 extends JFrame implements ActionListener {
    private JButton boton1, boton2;
    
    public Ej1() {
        setLayout(null);
        
        // Configuración Botón 1
        boton1 = new JButton("Varón");
        boton1.setBounds(10, 100, 90, 30);
        add(boton1);
        boton1.addActionListener(this);
        
        // Configuración Botón 2
        boton2 = new JButton("Mujer");
        boton2.setBounds(110, 100, 90, 30);
        add(boton2);
        boton2.addActionListener(this);
    }
    
    // Método que se dispara al pulsar cualquier botón
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == boton1) {
            // Cambiamos el título del JFrame usando el texto del botón
            setTitle("Varón");
        }
        if (e.getSource() == boton2) {
            setTitle("Mujer");
        }
    }
    
    public static void main(String[] ar) {
        Ej1 ventana = new Ej1();
        ventana.setBounds(0, 0, 300, 250);
        ventana.setVisible(true);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}