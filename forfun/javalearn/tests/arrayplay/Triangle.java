public class Triangle {
    public static void main(String[] args){

        int row = 0;
        int rows = 5;
        int charPerRow = 1;        
        while(row < rows){
            System.out.println("*".repeat(charPerRow));
            row++;
            charPerRow++;
        }
    }
}
