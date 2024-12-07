package forfun.javalearn.tests.JavaLibrary;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        Library lib = new Library();

        scanner.close();

        String[][] schema = 
        {{".displayBooks()",
        ".removeBook()",
        ".totalBooks()",
        ".copies()",
        ".findBook"},
        
        {"Display the books that are in the library,",
        "Remove a book from the library,",
        "Print how many different books there are,",
        "Print how many books there are in total,",
        "Find a specific book,"},
    
        {"1",
        "2",
        "3",
        "4",
        "5"}};

        System.out.println("What would you like to do?: ");
            
        for(int i = 0; i < schema[1].length; i++){
            System.out.println("In order to: " + schema[1][i] + " input: " + schema[2][i]);
        }
    }
}
