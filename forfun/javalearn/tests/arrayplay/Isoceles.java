public class Isoceles {
    public static void main(String[] args){
        int numberofrows = 10;
        int currentrow = 1;
        int charsperrow = 1;

        while(currentrow <= numberofrows){
            System.out.println(" ".repeat(numberofrows-currentrow) + "*".repeat(charsperrow));
            charsperrow += 2;
            currentrow++;
        }
    }
    
}
