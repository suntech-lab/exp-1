package forfun.javalearn.game.tile;

import java.awt.Graphics2D;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.FileReader;

import javax.imageio.ImageIO;

import forfun.javalearn.game.main.Javaday7panel;

public class TileManager {
    Javaday7panel gp;   
    public Tile[] tile;
    public int mapTileNum[][];

    public TileManager(Javaday7panel gp) {
        this.gp = gp;

        tile = new Tile[10];
        mapTileNum = new int[gp.maxWorldCol][gp.maxWorldRow];

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
            tile[2].collision = true;

            tile[4] = new Tile();
            tile[4].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/path.png"));

            tile[5] = new Tile();
            tile[5].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/water.png"));
            tile[5].collision = true;

            tile[6] = new Tile();
            tile[6].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/tree.png"));
            tile[6].collision = true;

            tile[7] = new Tile();
            tile[7].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/river.png"));
            tile[7].collision = true;

            tile[8] = new Tile();
            tile[8].image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/tiles/gravel.png"));

        }catch(IOException e) {
            e.printStackTrace();
        }
    }

    public void loadMap() {
        try {

            File is = new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/maps/map02.txt");
            if (is != null) {
                System.out.println("success");
            }
            BufferedReader br = new BufferedReader(new FileReader(is));

            int col = 0;
            int row = 0;

            while(col < gp.maxWorldCol && row < gp.maxWorldRow) {

                String line = br.readLine();

                while(col < gp.maxWorldCol) {

                    String numbers[] = line.split(" ");

                    int num = Integer.parseInt(numbers[col]);

                    mapTileNum[col][row] = num;
                    col++;
                }
                if(col == gp.maxWorldCol) {
                    col = 0;
                    row++;
                }
            }
            br.close();

        }catch(Exception e) {

        }
    }

    public void draw(Graphics2D g2) {

        int worldCol = 0;
        int worldRow = 0;

        while(worldCol < gp.maxWorldCol && worldRow < gp.maxWorldRow) {

            int tileNum = mapTileNum[worldCol][worldRow];

            int worldX = worldCol *gp.tileSize;
            int worldY = worldRow * gp.tileSize;
            int screenX = worldX - gp.player.worldX + gp.player.screenX;
            int screenY = worldY - gp.player.worldY + gp.player.screenY;

            if(worldX > gp.player.worldX - gp.player.screenX - gp.tileSize &&
                worldX < gp.player.worldX + gp.player.screenX + gp.tileSize &&
                worldY > gp.player.worldY - gp.player.screenY - gp.tileSize &&
                worldY < gp.player.worldY + gp.player.screenY + gp.tileSize) {
                g2.drawImage(tile[tileNum].image, screenX, screenY, gp.tileSize, gp.tileSize, null);
            }
            worldCol++;

            if (worldCol == gp.maxWorldCol) {
                worldCol = 0;
                worldRow++;
            }
        }
    }
}