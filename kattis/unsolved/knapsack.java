import java.util.Scanner;
import java.util.ArrayList;

public class knapsack {
    private static int[][] dp;
    private static int c, n;
    private static int[][] objs;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            c = in.nextInt();
            n = in.nextInt();
            objs = new int[n+1][2];
            for (int i = 1; i <= n; i++) {
                int v = in.nextInt();
                int w = in.nextInt();
                objs[i] = new int[] {v, w};
            }
            solve();
        }
        in.close();
    }

    private static void solve() {
        dp = new int[n+1][c+1];
        for (int i = 1; i <= n; i++) {
            int v = objs[i][0];
            int w = objs[i][1];

            if (w <= c) {
                dp[i][w] = Math.max(dp[i][w], v);
            }

            for (int j = 1; j <= c; j++) {
                dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
                if (j-w > 0 && dp[i-1][j-w] != 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j-w] + v);
                }
            }
        }

        // Find highest total when using all of the items
        int hi = 0, hiC = 1;
        for (int i = 1; i <= c; i++) {
            if (dp[n][i] > hi) {
                hi = dp[n][i];
                hiC = i;
            }
        }

        ArrayList<Integer> nums = new ArrayList<>();
        int hiI = n;
        while (hiC > 0) {
            while (dp[hiI][hiC] == dp[hiI-1][hiC]) {
                hiI--;
            }
            nums.add(hiI - 1);
            hiC -= objs[hiI][1];
        }

        System.out.println(nums.size());
        for (int num : nums) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}