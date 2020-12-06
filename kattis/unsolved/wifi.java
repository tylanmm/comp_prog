import java.io.*;
import java.util.*;

public class wifi {
    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader();
        int tests = in.nextInt();
        for (int t = 0; t < tests; t++) {
            int n = in.nextInt();
            int m = in.nextInt();
            int[] houses = new int[m];
            for (int i = 0; i < m; i++) {
                houses[i] = in.nextInt();
            }
            double ans = solve(n, m, houses);
            System.out.printf("%.1f\n", ans);
        }
        in.close();
    }

    private static double solve(int n, int m, int[] houses) {
        if (n >= m) {
            return 0.0;
        }

        Arrays.sort(houses);
        ArrayList<int[]> gaps = new ArrayList<int[]>(m-1);
        for (int i = 1; i < m; i++) {
            gaps.add(new int[] {houses[i] - houses[i-1], i-1, i});
        }

        // Sort based on gap size
        Collections.sort(gaps, (a, b) -> {
            return a[0] - b[0];
        });
        
        // Remove the largest gaps
        for (int i = 0; i < n-1; i++) {
            gaps.remove(gaps.size()-1);
        }
        
        // Sort based on starting coord
        Collections.sort(gaps, (a, b) -> {
            return a[1] - b[1];
        });

        // Find largest continuous stretch
        int start = 0;
        int prev = 0;
        int longestGap = 0;
        for (int i = 0; i < gaps.size(); i++) {
            if (gaps.get(i)[1] - 1 != prev) {
                longestGap = Math.max(longestGap, houses[prev] - houses[start]);
                start = gaps.get(i)[1];
            }
            prev = gaps.get(i)[1];
        }
        longestGap = Math.max(longestGap, houses[prev] - houses[start]);

        return longestGap / 2.0;
    }
}

class FastReader {
    private BufferedReader in;
    private String[] line = new String[0];
    private int pos = 0;

    public FastReader() throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
    }

    public void close() throws IOException {
        in.close();
    }

    public String[] nextLine() throws IOException {
        line = in.readLine().split(" ");
        pos = 0;
        return line;
    }

    public String next() throws IOException {
        while (pos == line.length) {
            nextLine();
        }

        return line[pos++];
    }

    public int nextInt() throws IOException {
        String val = next();
        return Integer.parseInt(val);
    }
}