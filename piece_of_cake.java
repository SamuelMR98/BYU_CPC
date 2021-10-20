import java.util.Scanner;

public class piece_of_cake {
    public static void main(String[] args) {
        int THICKNESS = 4;

        int side, hCut, vCut;
        Scanner in = new Scanner(System.in);

        side = in.nextInt();
        hCut = in.nextInt();
        vCut = in.nextInt();

        int slice1 = hCut * vCut * THICKNESS;
        int slice2 = hCut * (side - vCut) * THICKNESS;
        int slice3 = (side - hCut) * vCut * THICKNESS;
        int slice4 = (side - hCut) * (side - vCut) * THICKNESS;

        int maxAB, maxCD, max;

        maxAB = slice1 > slice2 ? slice1 : slice2;
        maxCD = slice3 > slice4 ? slice3 : slice4;
        max = maxAB > maxCD ? maxAB : maxCD;
    
        System.out.println(max);
    }
    
}
