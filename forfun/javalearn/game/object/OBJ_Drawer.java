package forfun.javalearn.game.object;

import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class OBJ_Drawer extends SuperObject {
        public OBJ_Drawer() {
        name = "Drawer";
        try{
            image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/objects/drawer.png"));
        
        }catch(IOException e){
            e.printStackTrace();
        }

    }

}
