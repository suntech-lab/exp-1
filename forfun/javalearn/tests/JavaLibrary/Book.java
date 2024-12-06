package forfun.javalearn.tests.JavaLibrary;

public class Book {
    String title;
    String author;
    int copies;

    public Book(String title, String author, int copies){
        this.title = title;
        this.author = author;
        this.copies = copies;
    }

    public String getTitle(){
        return title;
    }

    public String getAuthor(){
        return author;
    }

    public int getCopies(){
        return copies;
    }

    @Override

    public String toString(){
        return (title + " By: " + author + " (Copies: " + copies + ")");
    }
}
