package javalearn.game.tile;

import java.awt.Graphics2D;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.FileReader;

import javax.imageio.ImageIO;

import javalearn.game.main.Javaday7panel;

public class TileManager {
    Javaday7panel gp;
    Tile[] tile;
    int mapTileNum[][];

    public TileManager(Javaday7panel gp) {
        this.gp = gp;

        tile = new Tile[10];
        mapTileNum = new int[gp.maxScreenCol][gp.maxScreenRow];

        getTileImage();

        loadMap();
    }

    public void getTileImage() {
        try {

            tile[0] = new Tile();
            tile[0].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/grass.png"));

            tile[1] = new Tile();
            tile[1].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/wood.png"));

            tile[2] = new Tile();
            tile[2].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/wall.png"));

            tile[3] = new Tile();
            tile[3].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/door.png"));

            tile[4] = new Tile();
            tile[4].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/path.png"));

            tile[5] = new Tile();
            tile[5].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/water.png"));

        }catch(IOException e) {
            e.printStackTrace();
        }
    }
    public void loadMap() {
        try {

            File is = new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/maps/map01.txt");
            if (is != null) {
                System.out.println("success");
            }
            BufferedReader br = new BufferedReader(new FileReader(is));

            int col = 0;
            int row = 0;

            while(col < gp.maxScreenCol && row < gp.maxScreenRow) {

                String line = br.readLine();

                while(col < gp.maxScreenCol) {

                    String numbers[] = line.split(" ");

                    int num = Integer.parseInt(numbers[col]);

                    mapTileNum[col][row] = num;
                    col++;
                }
                if(col == gp.maxScreenCol) {
                    col = 0;
                    row++;
                }
            }
            br.close();

        }catch(Exception e) {

        }
    }

    public void draw(Graphics2D g2) {

        int col = 0;
        int row = 0;
        int x = 0;
        int y = 0;

        while(col < gp.maxScreenCol && row < gp.maxScreenRow) {

            int tileNum = mapTileNum[col][row];

            g2.drawImage(tile[tileNum].image, x, y, gp.tileSize, gp.tileSize, null);
            col++;
            x += gp.tileSize;

            if (col == gp.maxScreenCol) {
                col = 0;
                x = 0;
                row++;
                y += gp.tileSize;
            }
        }
    }
}
