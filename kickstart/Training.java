import java.util.*;
public class Training {
    public static int solve(ArrayList<Integer> nums, int p) {
        int total = 0;
        for (int i = 0; i < p; i++) {
            total += nums.get(p - 1) - nums.get(i);
        }

        int best = total;
        for (int i = 1; i <= nums.size() - p; i++) {
            total -= nums.get(i + p - 2) - nums.get(i - 1);                     // remove the training hours required to train the previous min skilled player to the previous group max
            total += (nums.get(i + p - 1) - nums.get(i + p - 2)) * (p - 1);     // add enough training hours for each player to make up the difference between the new skill cap and the previous
            best = Math.min(best, total);
        }

        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            int n = in.nextInt();
            int p = in.nextInt();
            ArrayList<Integer> nums = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                nums.add(in.nextInt());
            }
            nums.sort(null);
            System.out.println(String.format("Case #%d: %d", i+1, solve(nums, p)));
        }
    }
}