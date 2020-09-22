import java.util.*;
import java.io.*;

public class data {
    static int[] sieve = new int[14001];
    static int[] nums;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
        }
        in.close();
        
        genSieve();
        int total = 0;
        for (int num : nums) total += sieve[num];
        
        System.out.println(calc(0, total));
    }

    public static void genSieve() {
        for (int i = 2; i < 14001; i++) {
            if (sieve[i] > 0) {
                continue;
            }
            for (int j = i; j < 14001; j += i) {
                sieve[j] += 1;
            }
        }
    }

    public static int calc(int i, int total) {
        if (i == nums.length) return total;
        int hi = 0;
        for (int j = i+1; j < nums.length; j++) {
            int n1 = nums[i], n2 = nums[j];
            int s1 = sieve[n1], s2 = sieve[n2];
            if (s1 + s2 < 5 && sieve[n1 + n2] >= s1 + s2) {
                nums[j] += nums[i];
                hi = Math.max(hi, calc(i+1, total - s1 - s2 + sieve[n1 + n2]));
                nums[j] -= nums[i];
            }
        }
        return Math.max(hi, calc(i+1, total));
    }
}