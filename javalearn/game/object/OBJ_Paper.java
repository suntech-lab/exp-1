package javalearn.game.object;

import java.io.IOException;
import java.io.File;

import javax.imageio.ImageIO;

public class OBJ_Paper extends SuperObject{
    
    public OBJ_Paper() {
        name = "Paper";
        try{
            image = ImageIO.read(new File("C://Users/ericl/Documents/lab/forfun/javalearn/game/objects/paper.png"));
        
        }catch(IOException e){
            e.printStackTrace();
        }

    }

}
