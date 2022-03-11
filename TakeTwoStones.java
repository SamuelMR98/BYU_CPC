import java.util.Scanner;

public class TakeTwoStones {
    public static void main(String[] args) {
        Scanner io = new Scanner(System.in);

        int i = io.nextInt();

        if (i >= 1 && i <= 10000000) {
            i = i % 2;

            if (i == 0) {
                System.out.println("Bob");
            } else {
                System.out.println("Alice");
            }
        }

        io.close();
    }
}