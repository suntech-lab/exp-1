package javalearn.tests.primefinder;

import java.util.Scanner;

public class isitprime {
    public void is_it_prime(int prime_number) {
        if (prime_number <= 1) {
            System.out.println("No");
            return;
        }

        for (int x = 2; x <= Math.sqrt(prime_number) + 1; x++) {
            if (prime_number % x == 0) {
                System.out.println("No");
                return;
            }
        }
        System.out.println("Yes");
    }

    public int ask_input() {
        Scanner input = new Scanner(System.in);
        System.out.print("Number?: ");
        int prime_suspect = Integer.valueOf(input.nextLine());
        input.close();
        return prime_suspect;
    }
}