package javalearn.game.main;

import javalearn.game.object.OBJ_Door;
import javalearn.game.object.OBJ_Drawer;
import javalearn.game.object.OBJ_Paper;

public class AssetSetter {
    
    Javaday7panel gp;

    public AssetSetter(Javaday7panel gp) {
        this.gp = gp;
    }

    public void setObject() {

        gp.obj[0] = new OBJ_Paper();
        gp.obj[0].worldX = 12 * gp.tileSize;
        gp.obj[0].worldY = 9 * gp.tileSize;

        gp.obj[1] = new OBJ_Paper();
        gp.obj[1].worldX = 41 * gp.tileSize;
        gp.obj[1].worldY = 25 * gp.tileSize;

        gp.obj[2] = new OBJ_Door();
        gp.obj[2].worldX = 19 * gp.tileSize;
        gp.obj[2].worldY = 12 * gp.tileSize;

        gp.obj[3] = new OBJ_Door();
        gp.obj[3].worldX = 19 * gp.tileSize;
        gp.obj[3].worldY = 13 * gp.tileSize;

        gp.obj[4] = new OBJ_Door();
        gp.obj[4].worldX = 25 * gp.tileSize;
        gp.obj[4].worldY = 8 * gp.tileSize;

        gp.obj[5] = new OBJ_Door();
        gp.obj[5].worldX = 28 * gp.tileSize;
        gp.obj[5].worldY = 8 * gp.tileSize;
        
        gp.obj[6] = new OBJ_Door();
        gp.obj[6].worldX = 32 * gp.tileSize;
        gp.obj[6].worldY = 10 * gp.tileSize;
        
        gp.obj[7] = new OBJ_Door();
        gp.obj[7].worldX = 33 * gp.tileSize;
        gp.obj[7].worldY = 10 * gp.tileSize;
        
        gp.obj[8] = new OBJ_Drawer();
        gp.obj[8].worldX = 24 * gp.tileSize;
        gp.obj[8].worldY = 7 * gp.tileSize;
        
        gp.obj[9] = new OBJ_Drawer();
        gp.obj[9].worldX = 23 * gp.tileSize;
        gp.obj[9].worldY = 7 * gp.tileSize;
        
        gp.obj[10] = new OBJ_Drawer();
        gp.obj[10].worldX = 29 * gp.tileSize;
        gp.obj[10].worldY = 9 * gp.tileSize;
        
        gp.obj[11] = new OBJ_Drawer();
        gp.obj[11].worldX = 30 * gp.tileSize;
        gp.obj[11].worldY = 9 * gp.tileSize;
    }

}
