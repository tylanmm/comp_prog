import java.util.*;
import java.io.*;

public class irrigation {

    public static void main(String[] args) throws IOException {
        long start = System.nanoTime();
        
        // read input
        BufferedReader in = new BufferedReader(new FileReader("irrigation.in"));
        String[] line = in.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int c = Integer.parseInt(line[1]);
        int[][] points = new int[n][2];
        for (int i = 0; i < n; i++) {
            line = in.readLine().split(" ");
            points[i][0] = Integer.parseInt(line[0]);
            points[i][1] = Integer.parseInt(line[1]);
        }
        in.close();

        // generate edges
        ArrayList<int[]> edges = new ArrayList<int[]>();
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                int cost = dx*dx + dy*dy;
                if (cost >= c) {
                    edges.add(new int[] {i, j, cost});
                }
            }
        }
        
        
        // run kruskal's
        Collections.sort(edges, (a, b) -> { return a[2] - b[2]; });
        UFDS sets = new UFDS(n);
        int total = 0, i = 0, m = edges.size();
        while (n > 1 && i < m) {
            int[] top = edges.get(i++);
            if (sets.union(top[0], top[1])) {
                total += top[2];
                n--;
            }
        }
        
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("irrigation.out")));
        out.println(n == 1 ? total : -1);
        out.close();

        System.out.printf("%d ms\n", (System.nanoTime() - start) / (int) 1e6);
    }

    private static class UFDS {
        int[] p;
        int[] r;

        UFDS(int n) {
            p = new int[n];
            for (int i = 0; i < n; i++) p[i] = i;
            r = new int[n];
            for (int i = 0; i < n; i++) r[i] = 1;
        }

        int findSet(int u) {
            if (p[u] == u) return u;
            return p[u] = findSet(p[u]);
        }

        boolean union(int u, int v) {
            int pu = findSet(u), pv = findSet(v);
            if (pu != pv) {
                if (r[pu] > r[pv]) p[pv] = pu;
                else {
                    p[pu] = pv;
                    if (r[pu] == r[pv]) r[pv]++;
                }
                return true;
            }
            return false;
        }
    }
}