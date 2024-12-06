package forfun.javalearn.tests.JavaLibrary;
import java.util.List;
import java.util.ArrayList;

public class Library {

    List<Book> collection;

    public Library(){
        this.collection = new ArrayList<>();
    }

    public void addBook(Book book){
        collection.add(book);
    }

    public void removeBook(Book book){
    
        if(collection.contains(book)){
            System.out.println("\nRemoving one copy of " + book.title + " from the library...");
            book.copies -= 1;
            if(book.copies == 0){
                collection.remove(book);
            }
        }else{
            System.out.println("\nBook not found. Cannot remove.");
        }
        
    }

    public void findBook(String title){

        boolean found = false;
        System.out.println("\nFinding: " + title);

        for(Book book: collection){
            if(book.getTitle().equalsIgnoreCase(title)){    
                System.out.println(book);
                found = true;      
            }
        }

        if(found == false){
            System.out.println("Book not found.");
        }
    }

    public void displayBooks(){
        
        if(collection.isEmpty()){
            System.out.println("\nNothing in library.");
            return;
        }

        System.out.println("\nLibrary contains the following books:");

        for(Book book: collection){
            System.out.println(book);
        }
    }

    public void totalBooks(){
        System.out.println("\nTotal books: " + collection.size());
    }

    public void copies(){

        int tCopies = 0;
        
        for(Book book: collection){
            tCopies += book.copies;
        
        }
        System.out.println("\nTotal copies: " + tCopies);
    }
}
