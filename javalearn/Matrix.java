package javalearn;
public class Matrix {
    public static void main(String[] args){
        String[] names = {"anna", "billy", "eric", "matthew", "nicolas", "sarah"};
        String[] ages = {"16", "16", "15", "17", "17", "16"};
        int year = 2024;
        int yearend = 2024;


        int a;
        for(a = 0; a < ages.length; a++){

            int age = Integer.valueOf(ages[a]);
            age += yearend - year;
            ages[a] = String.valueOf(age);
        }

        int i;
        for(i = 0; i < names.length; i++){
            System.out.println(((names[i]+ " " + ages[i])));
        }
    }
}
