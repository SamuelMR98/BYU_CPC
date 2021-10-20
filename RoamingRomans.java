import java.util.Scanner;

public class RoamingRomans {
    public static void main(String[] args) {
        double miles;
        Scanner in = new Scanner(System.in);
        miles = in.nextDouble();
        double paces;
        paces = miles * (1000.0 * (5280.0/4854.0));
        System.out.println(Math.round(paces));    
    }
    
}
