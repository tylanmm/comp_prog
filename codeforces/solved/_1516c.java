import java.util.*;
import java.io.*;

public class _1516c {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        int tot = 0;
        for (int i = 0; i < n; i++) {
            a[i] = in.nextInt();
            tot += a[i];
        }
        in.close();
        
        if (tot % 2 == 1) System.out.println(0);
        else solve(a, tot);
    }

    public static void solve(int[] a, int tot) {
        boolean[][] dp = new boolean[a.length+1][(tot>>1)+1];
        dp[0][0] = true;
        for (int j = 0; j < tot>>1; j++) {
            for (int i = 0; i < a.length; i++) {
                dp[i+1][j] |= dp[i][j];
                if (dp[i][j] && (j + a[i] <= tot>>1)) {
                    dp[i+1][j + a[i]] = true;
                }
            }
        }
        
        if (!dp[a.length][tot>>1]) {
            System.out.println(0);
            return;
        }

        int lo = 0;
        int lsb = a[0] & -a[0];
        System.out.println(1);
        for (int i = 1; i < a.length; i++) {
            int LSB = a[i] & -a[i];
            if (LSB < lsb) {
                lo = i;
                lsb = LSB;
            }
        }

        System.out.println(lo+1);
    }
}