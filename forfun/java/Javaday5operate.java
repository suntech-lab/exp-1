package java;

public class Javaday5operate {
    public static void main(String[] args){
        Javaday5 anObj1 = new Javaday5();
        Javaday5 anObj2 = new Javaday5();
        System.out.println(anObj1.x);
        System.out.println(anObj1.doog);

        anObj1.x = 10;
        anObj1.doog = "good";

        System.out.println(anObj1.x);
        System.out.println(anObj2.x);
        System.out.println(anObj1.doog);

        //declared static
        Javaday5.myMethod();

        //declared public
        Javaday5 myObj = new Javaday5();
        myObj.otherMethod();

        //methods from object
        Javaday5 myCar = new Javaday5();
        myCar.fullThrottle();
        myCar.speed(200);
    }
}
