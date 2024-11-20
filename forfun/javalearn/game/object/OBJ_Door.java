package javalearn.game.object;

import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class OBJ_Door extends SuperObject{
        public OBJ_Door() {
        name = "Door";
        try{
            image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/objects/door.png"));
        
        }catch(IOException e){
            e.printStackTrace();
        }

    }

}
