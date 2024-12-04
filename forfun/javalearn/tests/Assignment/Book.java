package forfun.javalearn.tests.Assignment;

public class Book {
    String title;
    String author;
    int copies;

    public Book(String title, String author, int copies){
        this.title = title;
        this.author = author;
        this.copies = copies;
    }

    public String getTitle(String title){
        return title;
    }

    public String getAuthor(String author){
        return author;
    }

    public int getCopies(int copies){
        return copies;
    }

    public void setCopies(int copies){
        copies = 5;
    }

    public String toString(String title, String author, int copies){
        return ("Title: " + title + ", Author: " + author + ", Copies: " + copies);
    }
}
