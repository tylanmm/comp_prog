import java.io.*;
import java.util.*;

public class islandtour {
    static int n;
    static int[] dist;
    static int[] tij;
    static int[] ann;
    static int[] imm;

    public static void main(String[] args) {
        // read everything in
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        dist = new int[n];
        tij = new int[n];
        ann = new int[n];
        imm = new int[n];
        for (int i = 0; i < n; i++) dist[i] = in.nextInt();
        for (int i = 0; i < n; i++) tij[i] = in.nextInt();
        for (int i = 0; i < n; i++) ann[i] = in.nextInt();
        for (int i = 0; i < n; i++) imm[i] = in.nextInt();
        in.close();

        // set up prefix sums
        for (int i = 1; i < n; i++) {
            dist[i] += dist[i-1];
            tij[i] += tij[i-1];
            ann[i] += ann[i-1];
            imm[i] += imm[i-1];
        }

        // simulate, but be smart
        for (int t = 0; t < n; t++) {
            for (int a = 0; a < n; a++) {
                for (int i = 0; i < n; i++) {
                    // need to determine what order they're in somehow
                    boolean tai = (t < a && a < i) || (t < a && a < i+n) || (t < a+n && a < i);
                    int td = 0, ad = 0, id = 0;
                    while (t != a && t != i && td < n && ad < n && id < n) {
                        
                    }
                }
            }
        }
    }

    public static int sum(int a, int b, int[] arr) {
        return arr[b] + (a < b ? 0 : arr[n-1]) - (a > 0 ? arr[a-1] : 0);
    }
}