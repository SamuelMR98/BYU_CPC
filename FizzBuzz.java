import java.util.Scanner;

public class FizzBuzz {
    public static void main(String[] args) {
        int x, y, n;
        Scanner in = new Scanner(System.in);

        x = in.nextInt();
        y = in.nextInt();
        n = in.nextInt();
        int[] nums = new int[n];

        for (int i = 0; i < n; i++){
            nums[i] = i+1;
        }
        for (int i = 0; i < nums.length; i++){
            if ((nums[i] % x) == 0 && (nums[i] % y) != 0){
                System.out.println("Fizz");
            }else if ((nums[i] % y) == 0 && (nums[i] % x) != 0){
                System.out.println("Buzz");
            }else if((nums[i] % x) == 0 && (nums[i] % y) == 0){
                System.out.println("FizzBuzz");
            }else{
                System.out.println(nums[i]);
            }
        }
    }
}
