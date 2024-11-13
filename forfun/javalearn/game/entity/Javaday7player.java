package javalearn.game.entity;

import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;



public class Javaday7player extends Javaday7entity{
    javalearn.game.main.Javaday7panel gp;
    javalearn.game.main.Javaday7keyhandler keyH;

    public final int screenX;
    public final int screenY;

    public Javaday7player(javalearn.game.main.Javaday7panel gp, javalearn.game.main.Javaday7keyhandler keyH) {
        this.gp = gp;
        this.keyH = keyH;

        screenX = gp.screenWidth/2 - (gp.tileSize/2);
        screenY = gp.screenHeight/2 - (gp.tileSize/2);

        solidArea = new Rectangle();
        solidArea.x = 8;
        solidArea.y = 16;
        solidArea.width = 32;
        solidArea.height = 32;

        setDefaultValues();
        getPlayerImage();
    }
    public void setDefaultValues() {
        worldX = gp.tileSize * 23;
        worldY = gp.tileSize * 21;
        speed = 3;
        direction = "down";
    }
    public void getPlayerImage() {
        try {

            right1 = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/player/run1.png"));
            right2 = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/player/run2.png"));
            left1 = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/player/run3.png"));
            left2 = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/player/run4.png"));
            down1 = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/player/run5.png"));
            down2 = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/player/run6.png"));
            up1 = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/player/run7.png"));
            up2 = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/player/run8.png"));

        }catch(IOException e) {
            e.printStackTrace();
        }
    }
    public void update() {

        if (keyH.upPressed == true || keyH.downPressed == true ||
        keyH.leftPressed == true || keyH.rightPressed == true) {
            
            if (keyH.upPressed == true) {
                direction = "up";
            }
            if (keyH.downPressed == true) {
                direction = "down";
            }
            if (keyH.leftPressed == true) {
                direction = "left";
            }
             if (keyH.rightPressed == true) {
                direction = "right";
            }
    
            collisionOn = false;
            gp.cChecker.checkTile(this);

            //IF COLLISION IS FALSE, PLAYER CAN MOVE
            if(collisionOn == false) {
                switch(direction){
                    case "up": worldY -= speed; break;
                    case "down": worldY += speed; break;
                    case "left": worldX -= speed; break;
                    case "right": worldX += speed; break;
                }
            }

            spriteCounter++;
            if (spriteCounter > 12) {
                if (spriteNum == 1) {
                    spriteNum = 2;
                }
                else if (spriteNum == 2) {
                    spriteNum = 1;
                }
                spriteCounter = 0;
            }
        }
 }    
    public void draw(Graphics2D g2) {

        BufferedImage image = null;
        switch(direction) {
        case "up":
            if (spriteNum == 1) {
                image = up1;   
            }
            if (spriteNum == 2) {
                image = up2;
            }
            break;
        case "down":
            if (spriteNum == 1) {
                image = down1;
            }
            if (spriteNum == 2) {
                image = down2;
            }
            break;
        case "left":
            if (spriteNum == 1) {
                image = left1;
            }
            if (spriteNum == 2) {
                image = left2;
            }
            break;
        case "right":
            if (spriteNum == 1) {
                image = right1;
            }
            if (spriteNum == 2) {
                image = right2;
            }
            break;
        }
        g2.drawImage(image, screenX, screenY, gp.tileSize, gp.tileSize, null);

    }
}
