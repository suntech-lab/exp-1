package forfun.javalearn.tests.JavaLibrary;
import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Library lib = new Library();

        String[][] schema = 
       {{"Display the books that are in the library,",
        "Remove a book from the library,",
        "Print how many different books there are,",
        "Print how many books there are in total,",
        "Find a specific book,",
        "Add a book into the library,",
        "Exit"},
    
       {"0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6"}};
        
        Scanner scanner = new Scanner(System.in);

        while(true){
            System.out.println("What would you like to do?: ");

            for(int i = 0; i < schema[1].length; i++){
                System.out.println("In order to: " + schema[0][i] + " input: " + schema[1][i]);
            }
            
            String choice = scanner.nextLine();
            
            try{
                switch(Integer.valueOf(choice)){
                    case 0:
                        lib.displayBooks();
                        break;
                    
                    case 1:
                        lib.removeBook();
                        break;
                    
                    case 2:
                        lib.totalBooks();
                        break;
                    
                    case 3:
                        lib.copies();
                        break;
                    
                    case 4:
                        lib.findBook();
                        break;
                    
                    case 5:
                        lib.addBook();
                        break;
                    
                    case 6:
                        System.out.println("Exiting the program.");
                        scanner.close();
                        return;

                    default:
                        System.out.println("Invalid choice. Try again.");
                }

            }catch(Exception e){
                System.out.println("Invalid input. Please try again.");
            }
        }                
    }
}
