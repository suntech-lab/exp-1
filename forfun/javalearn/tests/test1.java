package forfun.javalearn.tests;

import java.util.Scanner;

public class test1 {
    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in);
        System.out.print("What is your username?: ");

        String userName = myObj.nextLine();
        System.out.println("Your username has been confirmed as: " + userName);

        myObj.close();
    }

}