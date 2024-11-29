package javalearn.tests.arrayplay;
public class Stopwatch{
    public static void main(String[] args) {
        long cTime;
        long lTime = System.nanoTime();
        long timeS = 0;
        int seconds = 0;
        while(true){
            cTime = System.nanoTime();
            timeS += (cTime-lTime);
            lTime = cTime;

            if(timeS >= 1000000000){
                seconds++;
                System.out.println(seconds);
                timeS = 0;
            }

            if(seconds >= 600){
                break;
            }
        }
    }
}
