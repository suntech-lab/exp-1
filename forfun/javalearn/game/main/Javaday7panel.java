package javalearn.game.main;

import java.awt.Color;
import java.awt.Dimension;
import javax.swing.JPanel;

import java.awt.Graphics;
import java.awt.Graphics2D;
import javalearn.game.entity.Javaday7player;
import javalearn.game.tile.TileManager;

public class Javaday7panel extends JPanel implements Runnable{
    final int originalTileSize = 16;
    final int scale = 3;

    public final int tileSize = originalTileSize*scale;
    public final int maxScreenCol = 16;
    public final int maxScreenRow = 12;
    public final int screenWidth = tileSize*maxScreenCol;
    public final int screenHeight = tileSize*maxScreenRow;

    //FPS
    int FPS = 60;

    TileManager tileM = new TileManager(this);
    Javaday7keyhandler keyH = new Javaday7keyhandler();
    Thread gameThread;
    Javaday7player player = new Javaday7player(this,keyH);

    public Javaday7panel() {
        this.setPreferredSize(new Dimension(screenWidth, screenHeight));
        this.setBackground(Color.black);
        this.setDoubleBuffered(true);
        this.addKeyListener(keyH);
        this.setFocusable(true);
        
    }

    public void startGameThread() {
        gameThread = new Thread(this);
        gameThread.start();
    }

    @Override
    public void run() {

        double drawInterval = 1000000000/FPS;
        double delta = 0;
        long lastTime = System.nanoTime();
        long currentTime;
        int drawCount = 0;
        long timer = 0;


        while (gameThread != null) {

            currentTime = System.nanoTime();

            delta += (currentTime - lastTime)/drawInterval;
            timer += (currentTime - lastTime);

            lastTime = currentTime;

            if (delta >= 1) {
                update();
                repaint();
                delta--;
                drawCount++;
            }

            if (timer >= 1000000000) {
                System.out.println("FPS: "+drawCount);
                drawCount = 0;
                timer = 0;
            }
        }
    }

    public void update() {
        player.update();
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D)g;

        tileM.draw(g2);
        player.draw(g2);

        g2.dispose();
    }
}