import java.util.Scanner;

public class scalingRecipes {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int cases = in.nextInt();

        for (int i = 0; i < cases; i++){
            int ingredients = in.nextInt();
            int portions = in.nextInt();
            int desiredPortions = in.nextInt();

            double scalingFactor = desiredPortions / portions;

            for (int j = 0; j < ingredients; j++){
                String name = in.next();
                double weight = in.nextDouble();
                double percentage = in.nextDouble();

                

                System.out.println(name + " ");


            }
            System.out.println("----------------------------------------");
        }

    }
    
}
