import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class stackingCups {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int Cups = Integer.parseInt(reader.readLine());

        List<Cup> cups = new ArrayList<>();

        while (Cups-- > 0) {
            String[] vals = reader.readLine().split(" ");

            if (vals[0].matches("\\d+")) {
                cups.add(new Cup(vals[1], Integer.parseInt(vals[0]) / 2));
            } else {
                cups.add(new Cup(vals[0], Integer.parseInt(vals[1])));
            }
        }

        Collections.sort(cups, (Cup c1, Cup c2) -> Integer.compare(c1.radius, c2.radius));

        cups.forEach((c) -> {
            System.out.println(c.color);
        });
    }

    public static class Cup {

        String color;
        int radius;

        Cup(String color, int radius) {
            this.color = color;
            this.radius = radius;
        }
    }
}
