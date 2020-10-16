import java.io.*;
import java.util.*;

public class _1385e {
    static ArrayList<ArrayList<Integer>> g;
    static boolean[] visited;
    static ArrayList<Integer> order;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        for (int z = 0; z < t; z++) {
            String[] line = in.readLine().split(" ");
            int n = Integer.parseInt(line[0]), m = Integer.parseInt(line[1]);
            g = new ArrayList();
            for (int i = 0; i < n; i++) {
                g.add(new ArrayList());
            }

            int[][] edges = new int[m][2];
            for (int i = 0; i < m; i++) {
                line = in.readLine().split(" ");
                int type = Integer.parseInt(line[0]);
                int x = Integer.parseInt(line[1]), y = Integer.parseInt(line[2]);
                x--; y--;
                edges[i][0] = x;
                edges[i][1] = y;
                if (type == 1) {
                    g.get(x).add(y);
                }
            }

            visited = new boolean[n];
            order = new ArrayList();
            for (int i = 0; i < n; i++) {
                if (!visited[i]) {
                    topo(i);
                }
            }
            Collections.reverse(order);

            int[] pos = new int[n];
            for (int i = 0; i < n; i++) {
                pos[order.get(i)] = i;
            }

            boolean hasCycle = false;
            for (int i = 0; i < n; i++) {
                for (int node : g.get(i)) {
                    if (pos[i] > pos[node]) {
                        hasCycle = true;
                    }
                }
            }

            if (hasCycle) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
                for (int i = 0; i < m; i++) {
                    if (pos[edges[i][0]] < pos[edges[i][1]]) {
                        System.out.println((edges[i][0] + 1) + " " + (edges[i][1] + 1));
                    } else {
                        System.out.println((edges[i][1] + 1) + " " + (edges[i][0] + 1));
                    }
                }
            }
        }
        in.close();
    }

    public static void topo(int node) {
        visited[node] = true;
        for (int neighbor : g.get(node)) {
            if (!visited[neighbor]) {
                topo(neighbor);
            }
        }
        order.add(node);
    }
}