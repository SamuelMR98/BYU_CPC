import java.util.Scanner;

public class modulo{
    public static void main(String[] args) {
        int[] nums = new int[10];
        int counter = 0;
        Scanner in = new Scanner(System.in);
        for(int i = 0; i < 10; i ++){
            nums[i] = in.nextInt();
        }
        
        for (int i = 0; i < nums.length; i++){

            if ((nums[i] % 42) == nums[i]){
                counter++;
            }else if(counter == 0){

            }
        }

    }
}