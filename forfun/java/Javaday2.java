package forfun.java;
public class Javaday2 {
    public static void main(String[] args) {
        //primitive numbers can be divided into two types
        //integers and decimals
        //floats can be used to write scientific numbers
        //boolean data types
        //char can store ascii values as well as single characters

        int totalItems = 50;
        float itemCost = 5.99f;
        double totalCost = totalItems*itemCost;
        System.out.println(totalCost);

        //non primitive data types
        //they are created by the programmer, except String
        //all primitive have to have a value except for non, which can be null
        //non primitive types start with capital
        //strings, classes, arrays, interface

        //casting
        //casting is when you change the data type of something to another
        //widening, narrowing

        int narrowInt = 9;
        float wideInt = narrowInt;
        System.out.println(narrowInt);
        System.out.println(wideInt);

        float wideFloat = 9.9f;
        int narrowFloat = (int)wideFloat;
        System.out.println(wideFloat);
        System.out.println(narrowFloat);

        //operators
        int increment = 5;
        ++increment;
        System.out.println(increment);
        --increment;
        System.out.println(increment);

        //&&
        //^and
        //||
        //^or
        //!
        //^not

        //Strings
        String blah = "onE two THREE four";
        System.out.println(blah.length());
        System.out.println(blah.toUpperCase());
        System.out.println(blah.toLowerCase());
        System.out.println(blah.indexOf("THREE"));

        //concatenation same as python
        //new concat() method

        String blahah = "Jon";
        String gah = "Garfield";
        String fargield = blahah.concat(gah);
        System.out.println(fargield);

        //math
        System.out.println(Math.max(100, 2));
        System.out.println(Math.min(100, 2));
        System.out.println(Math.sqrt(100));
        System.out.println(Math.abs(-10000000));
        System.out.println(Math.random());

        //boolean same as python

        //if, else, if...else

        double randomNumber = Math.random();

        if (randomNumber <= 0.3)
        {
            System.out.println("give me lasagna");
        } else if (randomNumber > 0.6) {
            System.out.println("im not ungry");
        } else {
            System.out.println("i need sugar");
        }

        //ternary operator

        //variable = definition;
        //variable = (condition) ? "potential value": "potential value";

        String result = (randomNumber < 0.2) ? "randomNumber is less than 0.2": "randomNumber is larger than 0.2";
        System.out.println(result);

    }
    }

//Completed W3Schools Java Tutorial Java Data Types-If...Else