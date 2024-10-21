package forfun.java;
//this is a comment, two forward slashes
public class Javaday1 {//file has the same name as the public class
    public static void main(String[] args) {
        System.out.println("Hello World");
        System.out.println("curly brackets signify the start and end of one block of code");
        System.out.println("third \'System.out.println()\'");
        System.out.println("everything inside");

        System.out.println((124+1)*4);

        String string = "first string";
        int number = 123;
        System.out.println(string);
        System.out.println(number);

        int assignint;
        assignint = 15;
        assignint = 30;
        System.out.println(assignint);

        final int finalint = 60; //final integers cannot be reassigned, ers otherwise.
        System.out.println(finalint);

        float floater = 5.5f;
        char letter = 'E';
        boolean bool = true;
        String text = "yeap";
        System.out.println(floater);
        System.out.println(letter);
        System.out.println(text);
        System.out.println(bool);
        
        System.out.println(text + string);
        String firstname = "Eric ";
        String chinesename = "Sun Hao Yang ";
        String lastname = "Liu ";
        String fullname = firstname + chinesename + lastname;
        System.out.println(fullname);

        int x = 5;
        int y = 1;
        int sum = x + y;
        System.out.println(sum);

        int t = 10, d = 100, v = d/t;
        System.out.println(v);

        int a, b, c;
        a = b = c = 1;
        System.out.println(a + b + c);

        String studentName = "Eric";
        char studentGrade = 'A';
        int studentAge = 15;
        System.out.println("Student Name: " + studentName);
        System.out.println("Student Grade: " + studentGrade);
        System.out.println("Student Age: " + studentAge);

        //primitive data types
        byte testByte1 = -128;
        byte testByte2 = 127;
        short testShort1 = -32768;
        short testShort2 = 32767;
        int testInt1 = -2147483648;
        int testInt2 = 2147483647;
        long testLong1 = 1;
        long testLong2 = -1;
        float testFloat = 4.5f;
        double testDouble = 4.55555555;
        boolean testBool = true;
        char testChar = 'G';
        System.out.println(testByte1);
        System.out.println(testByte2);
        System.out.println(testShort1);
        System.out.println(testShort2);
        System.out.println(testInt1);
        System.out.println(testInt2);
        System.out.println(testLong1);
        System.out.println(testLong2);
        System.out.println(testFloat);
        System.out.println(testDouble);
        System.out.println(testBool);
        System.out.println(testChar);

        }
}
/*
 * multi-line comments start with "/*"
 * have an asterisk at the start of every line
 * and end with
 */

 /*
  * Completed W3Schools Java Tutorial Java Home-Variables
  */