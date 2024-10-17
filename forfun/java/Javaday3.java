public class Javaday3 {
    public static void main(String[] args) {
        
        //switch and break
        int r = 3;
        switch (r) {
            case 1:
                System.out.println("r is 1");
                break;
            case 2:
                System.out.println("r is 2");
                break;
            default:
            System.out.println("r is neither 1 or two");
        }

        //while loop
        int t = 0;
        while (t <= 10) {
            System.out.println(t);
            t++;
        }
        t = 0;

        //do/while loop
        do {
            System.out.println(t);
            t--;
        }
        while (t >= -10);

        //for loop
        for (t = 0; t <= 10; t++) {
            System.out.println(t);
        }

        //nested loops
        for (t = 0; t <= 2; t++){
            System.out.println("outer");
            for (int a = 1; a <= 3; a++){
                System.out.println("inner");
            }
        }

        //for each loop
        int[] l = {1, 2, 3, 4};
        for (int a: l){
            System.out.println(a);
        }

        //break and continue
        for (t = 0; t < 10; t++){
            if (t > 5){
                break;
            }
            System.out.println(t);
        }

        for (t = 0; t <= 10; t++){
            if (t == 4){
                continue;
            }
            System.out.println(t);
        }

        //arrays
        //define variable type with square brackets to make an array
        String[] names = {"anna", "brockton", "carlos", "diana", "eric"};
        char[] letters = {'a', 'b', 'c', 'd', 'e'};
        for (String j: names){
            System.out.println(j);
            for (char i: letters){
                System.out.println(i);
            }
        }
        names[1] = "";
        names[2] = "";
        names[3] = "";
        for (String j: names){
            System.out.println(j);
        }
        System.out.println(names.length);

        for (t = 1; t <= names.length; t++){
            System.out.println(t);
        }
        for (String h: names){
            System.out.println(h);
        }

        int[] ages = {15, 16, 18, 20, 51};
        float avg, sum = 0;
        int length = ages.length;
        for (int age: ages){
            sum += age;
        }
        avg = sum/length;
        System.out.println(avg);

        int[][][] threedimensions = {{{1,2,3}, {4,5,6}, {7,8,9}},{{10,11,12}, {13,14,15}, {16,17,18}}, {{19,20,21}, {22,23,24}, {25,26,27}}};
        System.out.println(threedimensions[2][2][2]);
    }
}

//Completed W3Schools Java tutorial Java Switch-Arrays