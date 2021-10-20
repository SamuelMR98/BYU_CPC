import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class beenEverywhereMan {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int cases = in.nextInt();

        for (int i = 0; i < cases; i++){
            int cities = in.nextInt();
            Set<String> cityList = new HashSet<String> ();

            for (int j = 0; j < cities; j ++){
                String city = in.next();
                cityList.add(city);
            }
            System.out.println(cityList.size());
            cityList.clear();
        }


    }
    
}
