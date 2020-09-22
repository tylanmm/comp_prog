/*
ID: tylan071
LANG: JAVA
TASK: holstein
*/

import java.io.*;
import java.util.*;

class holstein {
    public static int v;
    public static int[] vit;
    public static int g;
    public static int[][] feeds;
    public static ArrayList<Integer> ans = new ArrayList<Integer>();

    public static void main(String[] args) throws IOException {
        read();
        solve();
        write();
    }

    public static void solve() {
        for (int k = 0; k < (int) Math.pow(2, g); k++) {
            int[] amts = new int[v];
            ArrayList<Integer> feedsUsed = new ArrayList<Integer>();
            int set = k;
            for (int i = 0; i < g; i++) {
                if (set % 2 == 1) {
                    feedsUsed.add(i+1);
                    for (int j = 0; j < v; j++) {
                        amts[j] += feeds[i][j];
                    }
                }
                set /= 2;
            }

            boolean isValid = true;
            for (int i = 0; i < v; i++) {
                if (amts[i] < vit[i]) {
                    isValid = false;
                    break;
                }
            }

            if (isValid && feedsUsed.size() < ans.size()) {
                ans = feedsUsed;
            }
        }
    }

    public static void read() throws IOException {
        Scanner in = new Scanner(new File("holstein.in"));

        v = in.nextInt();
        vit = new int[v];
        for (int i = 0; i < v; i++) {
            vit[i] = in.nextInt();
        }

        g = in.nextInt();
        feeds = new int[g][v];
        for (int i = 0; i < g; i++) {
            for (int j = 0; j < v; j++) {
                feeds[i][j] = in.nextInt();
            }
        }

        for (int i = 0; i <= g; i++) ans.add(0);

        in.close();
    }

    public static void write() throws IOException {
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("holstein.out")));
        out.print(ans.size());
        for (int i = 0; i < ans.size(); i++) {
            out.print(" " + ans.get(i));
        }
        out.println();
        out.close();
    }
}