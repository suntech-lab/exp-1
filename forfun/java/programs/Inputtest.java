import java.util.Scanner;

public class Inputtest {
    public static void main(String[] args){
        Scanner scannerObj = new Scanner(System.in);
        System.out.println("Enter username: ");

        String userName = scannerObj.nextLine();
        System.out.println("Username is: " + userName);
    }
    
}
