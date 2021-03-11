import java.util.*;
import java.io.*;

public class _1490e {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(in.readLine());
            String[] nums = in.readLine().split(" ");
            int[][] a = new int[n][2];
            for (int j = 0; j < n; j++) {
                a[j][0] = Integer.parseInt(nums[j]);
                a[j][1] = j+1;
            }
            Arrays.sort(a, (x, y) -> {
                return y[0] - x[0];
            });
            
            int left = a[0][0];
            int prev = 0;
            int pending = 0;
            long total = 0;
            for (int[] num : a) total += num[0];
            ArrayList<Integer> ans = new ArrayList<Integer>();
            for (int j = 0; j < n; j++) {
                if (a[j][0] != prev) {
                    total -= pending;
                    pending = a[j][0];
                } else {
                    pending += prev;
                }
                prev = a[j][0];

                if (total >= left) {
                    ans.add(a[j][1]);
                    left = a[j][0];
                } else {
                    break;
                }
            }

            Collections.sort(ans);
            System.out.println(ans.size());
            for (int id : ans) {
                System.out.print(id + " ");
            }
            System.out.println();
        }
    }
}