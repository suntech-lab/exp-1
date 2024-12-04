package forfun.javalearn.tests.Assignment;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Library {

    String[] collection;

    public Library(String[] collection){
        this.collection = collection;
    }

    public void addBook(Book book){
        List<String> collection = new ArrayList<String>();
        collection.add(toString());
    }

    public void removeBook(Book book){
        List<String> collection = new ArrayList<String>();
        collection.remove(toString());
    }

    public void findBook(Book book){
        List<String> collection = new ArrayList<String>();
        /*
        if(collection.contains(Book title)){
            System.out.println(book);
        }
         */
    }
}
