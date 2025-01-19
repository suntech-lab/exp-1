package forfun.javalearn.tests.JavaLibrary;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Library {
    Scanner scanner;
    List<Book> collection;

    public Library(){
        this.collection = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    public static String capitalizeWords(String input){
        if (input == null || input.isEmpty()){
            return input;
        }
        String[] words = input.split("\\s");
        StringBuilder result = new StringBuilder();
        for (String word : words){
            result.append(Character.toUpperCase(word.charAt(0))).append(word.substring(1).toLowerCase()).append(" ");
        }
        return result.toString().trim();
    }

    public void addBook(){
        System.out.println("Book title?: ");
        String title = capitalizeWords(scanner.nextLine());
        System.out.println("Book author?: ");
        String author = capitalizeWords(scanner.nextLine());
        System.out.println("How many copies to add?: ");
        try{
            int copies = Integer.valueOf(scanner.nextLine());
            Book book = new Book(title, author, copies);
            collection.add(book);
            System.out.println(title + " Added.");
        }catch (Exception e){
           System.out.println("Invalid input for copies. Sorry!");
           return;
        }
    }

    public boolean removeBook(){
        System.out.println("What is the title of the book you want to remove?: ");
        String title = scanner.nextLine();
        Book book = getBook(title);
        if(collection.contains(book)){
            System.out.println("\nRemoving one copy of " + book.title + " from the library...");
            book.copies -= 1;
            if(book.copies == 0){
                collection.remove(book);
            }
            return true;
        }else{
            System.out.println("\nBook not found. Cannot remove.");
            return false;
        }
        
    }

    public Book getBook(String title){
        for(Book book: collection){
            if(book.getTitle().equalsIgnoreCase(title)){  
                return book;
            }
        }
        return null;
    }

    public void findBook(){
        System.out.println("What is the title of the book you want to find?: ");
        String title = scanner.nextLine();
        Book book = getBook(title);
        if(book != null){
            System.out.println(book);
        }else{
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
