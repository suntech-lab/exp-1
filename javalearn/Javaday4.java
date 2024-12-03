package javalearn;
public class Javaday4 {
    static void myMethod(){
        System.out.println("myMethod has been executed.");
    }
    static int addition(int x, int y){
        return x + y;
    }
    static void checkNumber(int x){
        if (x < 21){
            System.out.println("Not allowed to drink in America.");
        } else {
            System.out.println("Allowed to drink in America.");
        }
    }
    static int methodOverload(int x, int y){
        return x + y;
    }
    static double methodOverload(double x, double y){
        return x + y;
    }
    static int fibonacci(int x){
        if (x <= 1){
            return x;
        }
        return fibonacci(x - 1) + fibonacci(x - 2);
    }
    
    public static void main(String[] args){
        myMethod();
        myMethod();
        myMethod();
        int x = addition(123, 321);
        System.out.println(x);

        checkNumber(21);

        int a = methodOverload(6, 1);
        double b = methodOverload(5.5, 4.5);
        System.out.println(a);
        System.out.println(b);

        int y = fibonacci(10);
        System.out.println(y);
    }
}

//Completed W3Schools Java Methods