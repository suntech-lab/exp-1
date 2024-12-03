package javalearn;
import java.util.Arrays;

public class Goofyarray {
    public static void main(String[] args){
        int[] ages = {15, 16, 21};
        int currentyear = 2024;
        int year = 2026;
        int i = 0;

        for(i = 0; i < ages.length; i++){
             ages[i] += year - currentyear;
        }

        System.out.println(Arrays.toString(ages));
    }   
}
