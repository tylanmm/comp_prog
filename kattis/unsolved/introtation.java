import java.io.*;
import java.util.*;

public class introtation {
    static int[] left = new int[1000001];
    static int[] right = new int[1000001];
    public static void main(String[] args) throws IOException {
        getAllCounts();
        
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            System.out.println(query(a, b));
        }
        in.close();
    }

    private static int query(int lo, int hi) {
        return left[hi] - (right[1] - right[lo+1]);
    }

    private static void getAllCounts() {
        for (int i = 1; i < 1000001; i++) {
            getCounts(i);
        }

        for (int i = 2; i < 1000001; i++) {
            left[i] += left[i-1];
        }

        for (int i = 999999; i >= 0; i--) {
            right[i] += right[i+1];
        }
    }

    private static void getCounts(int n) {
        int lo = (int) Math.pow(10, Integer.toString(n).length()-1);
        int digit = 10;
        HashSet<Integer> lefts = new HashSet<Integer>();
        HashSet<Integer> rights = new HashSet<Integer>();
        
        while (digit < n) {
            int newNum = (n % digit) * digit + (n / digit);
            if (lo <= newNum && newNum < lo*10) {
                if (n < newNum) {
                    rights.add(newNum);
                } else {
                    lefts.add(newNum);
                }
            }
            digit *= 10;
        }

        for (int num : lefts) {
            right[num]++;
        }

        for (int num : rights) {
            left[num]++;
        }
    }
}