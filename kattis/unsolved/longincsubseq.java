import java.io.*;
import java.util.*;

public class longincsubseq {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line = in.readLine();
        while (line != null) {
            int n = Integer.parseInt(line);
            String[] numLine = in.readLine().split(" ");
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = Integer.parseInt(numLine[i]);
            }
            solve(n, nums);
        }
    }

    private static void solve(int n, int[] nums) {
        int[] sub = new int[n+1];
        int length = 1;
        for (int i = 1; i < n; i++) {
            for (int j = length - 1; j >= 0; j--) {
                if (nums[i] < nums[sub[j]]) {
                    
                }
            }
        }
    }
}
