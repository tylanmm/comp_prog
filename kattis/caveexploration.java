import java.util.Scanner;

public class caveexploration {
    private static ArrayList<Integer>[] g;
    private static int[] num;
    private static int[] low;
    private static int[] parent;
    private static int visited;
    private static
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        g = new ArrayList[n];
        for (int i = 0; i < m; i++) {
            int u = in.nextInt();
            int v = in.nextInt();
            if (g[u] == null) {
                g[u] = new ArrayList<Integer>();
            }
            if (g[v] == null) {
                g[v] = new ArrayList<Integer>();
            }
            g[u].add(v);
            g[v].add(u);
        }
        in.close();


    }
}
