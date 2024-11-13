package javalearn.game.main;

import javax.swing.JFrame;

public class Javaday7 {

    public static void main(String[] args) {

        JFrame window = new JFrame();
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setResizable(false);
        window.setTitle("cool game");

        Javaday7panel javaday7panel = new Javaday7panel();
        window.add(javaday7panel);

        window.pack();

        window.setLocationRelativeTo(null);
        window.setVisible(true);

        javaday7panel.startGameThread();

    }

}
//https://www.youtube.com/watch?v=Ny_YHoTYcxo
