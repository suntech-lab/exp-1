import java.util.Arrays;

public class Matrix {
    public static void main(String[] args){
        String[] names = {"eric", "anna", "matthew", "nicolas"};
        String[] ages = {"15", "16", "17", "17"};
        int year = 2024;
        int yearend = 2024;

        String[][] info = {names, ages};
        System.out.println(Arrays.toString(info));
    }
}
