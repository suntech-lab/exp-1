package javalearn.game.main;

import javalearn.game.object.OBJ_Paper;

public class AssetSetter {
    
    Javaday7panel gp;

    public AssetSetter(Javaday7panel gp) {
        this.gp = gp;
    }

    public void setObject() {

        gp.obj[0] = new OBJ_Paper();
        gp.obj[0].worldX = 23 * gp.tileSize;
        gp.obj[0].worldY = 9 * gp.tileSize;

        gp.obj[1] = new OBJ_Paper();
        gp.obj[1].worldX = 81 * gp.tileSize;
        gp.obj[1].worldY = 25 * gp.tileSize;

    }

}
