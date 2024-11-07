package java.game.entity;

import java.awt.Graphics2D;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;



public class Javaday7player extends Javaday7entity{
    java.game.main.Javaday7panel gp;
    java.game.main.Javaday7keyhandler keyH;

    public Javaday7player(java.game.main.Javaday7panel gp, java.game.main.Javaday7keyhandler keyH) {
        this.gp = gp;
        this.keyH = keyH;

        setDefaultValues();
        getPlayerImage();
    }
    public void setDefaultValues() {
        x = 100;
        y = 100;
        speed = 4;
        direction = "down";
    }
    public void getPlayerImage() {
        try {

            right1 = ImageIO.read(new File("C:/Users/ericl/Documents/lab/java/player/run1.png"));
            right2 = ImageIO.read(new File("C:/Users/ericl/Documents/lab/java/player/run2.png"));
            left1 = ImageIO.read(new File("C:/Users/ericl/Documents/lab/java/player/run3.png"));
            left2 = ImageIO.read(new File("C:/Users/ericl/Documents/lab/java/player/run4.png"));
            down1 = ImageIO.read(new File("C:/Users/ericl/Documents/lab/java/player/run5.png"));
            down2 = ImageIO.read(new File("C:/Users/ericl/Documents/lab/java/player/run6.png"));
            up1 = ImageIO.read(new File("C:/Users/ericl/Documents/lab/java/player/run7.png"));
            up2 = ImageIO.read(new File("C:/Users/ericl/Documents/lab/java/player/run8.png"));

        }catch(IOException e) {
            e.printStackTrace();
        }
    }
    public void update() {
        if (keyH.upPressed == true) {
            direction = "up";
            y -= speed;
        }
        if (keyH.downPressed == true) {
            direction = "down";
            y += speed;
        }
        if (keyH.leftPressed == true) {
            direction = "left";
            x -= speed;
        }
         if (keyH.rightPressed == true) {
            direction = "right";
            x += speed;
        }
    }
    public void draw(Graphics2D g2) {

        BufferedImage image = null;
        switch(direction) {
        case "up":
            image = up1;
            break;
        case "down":
            image = down1;
            break;
        case "left":
            image = left1;
            break;
        case "right":
            image = right1;
            break;
        }
        g2.drawImage(image, x, y, gp.tileSize, gp.tileSize, null);

    }
}
