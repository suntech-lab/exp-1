package forfun.javalearn.tests;
public class Array {
    public static void main(String[] args){
        String[] array1 = {"apple","banana","pinapple"};

        for(int i = 0; i <= array1.length; i++){

            try {
                System.out.println(array1[i]);
            } catch (Exception e) {
                break;
            }
        }
    }
}
