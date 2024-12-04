package forfun.javalearn.game.main;

import forfun.javalearn.game.object.OBJ_Door;
import forfun.javalearn.game.object.OBJ_Drawer;
import forfun.javalearn.game.object.OBJ_Paper;

public class AssetSetter {
    
    Javaday7panel gp;

    public AssetSetter(Javaday7panel gp) {
        this.gp = gp;
    }

    public void setObject() {

        gp.obj[0] = new OBJ_Door();
        gp.obj[0].worldX = 9 * gp.tileSize;
        gp.obj[0].worldY = 7 * gp.tileSize;

        gp.obj[1] = new OBJ_Door();
        gp.obj[1].worldX = 3 * gp.tileSize;
        gp.obj[1].worldY = 7 * gp.tileSize;

        gp.obj[2] = new OBJ_Door();
        gp.obj[2].worldX = 16 * gp.tileSize;
        gp.obj[2].worldY = 7 * gp.tileSize;
        
        gp.obj[3] = new OBJ_Door();
        gp.obj[3].worldX = 18 * gp.tileSize;
        gp.obj[3].worldY = 9 * gp.tileSize;

        gp.obj[4] = new OBJ_Door();
        gp.obj[4].worldX = 3 * gp.tileSize;
        gp.obj[4].worldY = 12 * gp.tileSize;
        
        gp.obj[5] = new OBJ_Door();
        gp.obj[5].worldX = 0 * gp.tileSize;
        gp.obj[5].worldY = 20 * gp.tileSize;
        
        gp.obj[6] = new OBJ_Door();
        gp.obj[6].worldX = 0 * gp.tileSize;
        gp.obj[6].worldY = 19 * gp.tileSize;

    }

}
