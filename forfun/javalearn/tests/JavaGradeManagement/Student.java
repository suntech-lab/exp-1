package forfun.javalearn.tests.JavaGradeManagement;

import java.util.ArrayList;

public class Student {
    String name;
    ArrayList<String> grades;

    public Student(String name, ArrayList<String> grades){
        this.name = name;
        this.grades = grades;
    }

    public String getName(String name){
        return name;
    }

    public ArrayList<String> getGrades(ArrayList<String> grades){
        return grades;
    }

    public ArrayList<String> setGrades(ArrayList<String> newGrades){
        grades = newGrades;
        return grades;
    }

    @Override

    public String toString(){
        return ("Name: " + name + ", Grades: " + grades);
    }
}
