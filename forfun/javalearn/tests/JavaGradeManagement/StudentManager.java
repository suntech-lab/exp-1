package forfun.javalearn.tests.JavaGradeManagement;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class StudentManager {
    ArrayList<Student> students;

    public StudentManager(ArrayList<Student> students){
        this.students = students;
    }

    public void addStudent(Student student){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Student name?: ");
        student.name = scanner.nextLine();
        System.out.println("Student Grades?: ");
        student.grades.add(scanner.nextLine());
        students.add(student);
        scanner.close();
    }

    public void removeStudent(Student student){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Name of to-be-removed student?: ");
        student.name = scanner.nextLine();
        students.remove(student);
        scanner.close();
    }

    public void updateGrades(ArrayList<String> newGrades, Student student){
        Scanner scanner = new Scanner(System.in);
        int grade = 1;
        while(grade < 8){
            System.out.println("Grade #" + grade + ": ");
            try {
                Integer.valueOf(scanner.nextLine());
                newGrades.add(scanner.nextLine());
            } catch (Exception e) {
                System.out.println("Non integer grade detected. Try again.");
                grade--;
            }
            grade++;
        }
        student.setGrades(newGrades);
        scanner.close();
    }

    public ArrayList<String> displayStudents(ArrayList<String> students){
        return students;
    }

    public int calculateAverage(Student student){
        int accumulate = 0;
        for(int i = 0; i < 8; i++){
            accumulate += Integer.valueOf(student.grades.get(i));
        }
        return accumulate/8;
    }

    public Student getHighestGrade(Student student){//needs work
        for(int i = 0; i < students.size(); i++){
            System.out.println(students.get(i));
        }
        return student;
    }

    public Student getLowestGrade(Student student){//needs work
        for(int i = 0; i < students.size(); i++){
            System.out.println(students.get(i));
        }
        return student;
    }

    public Student searchStudent(String name){
        for(int i = 0; i < students.size(); i++){
            
        }
    }
}
