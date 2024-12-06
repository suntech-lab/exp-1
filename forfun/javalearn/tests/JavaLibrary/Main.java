package forfun.javalearn.tests.JavaLibrary;

public class Main {
    public static void main(String[] args){
        Library lib = new Library();
        Book book1 = new Book("the Silence that Binds Us", "Joanna Ho", 3);
        Book book2 = new Book("Six Crimson Cranes", "Elizabeth Lim", 1);
        Book book3 = new Book("the Night Wanderer", "Drew Hayden Taylor", 5);

        lib.addBook(book1);
        lib.addBook(book2);
        lib.addBook(book3);

        lib.displayBooks();

        lib.removeBook(book1);

        lib.findBook("the silence that binds us");

        lib.totalBooks();

        lib.copies();
    }
}
