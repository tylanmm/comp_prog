import java.util.ArrayDeque;
import java.util.Scanner;

public class ecoins {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
            int m = in.nextInt();
            int S = in.nextInt();
            int[][] coins = new int[m][2];
            for (int j = 0; j < m; j++) {
                coins[j][0] = in.nextInt();
                coins[j][1] = in.nextInt();
            }
            System.out.println(bfs(coins, S));
        }
        in.close();
    }

    private static String bfs(int[][] coins, int S) {
        boolean[][] seen = new boolean[S+1][S+1];
        ArrayDeque<int[]> q = new ArrayDeque<int[]>();
        q.add(new int[] {0, 0, 0});
        while (!q.isEmpty()) {
            int[] top = q.poll();
            double dist = Math.sqrt(top[0]*top[0] + top[1]*top[1]);
            if (dist > S || seen[top[0]][top[1]]) {
                continue;
            }
            seen[top[0]][top[1]] = true;
            if (Math.abs(dist - S) < 0.000001) {
                return Integer.toString(top[2]);
            }

            for (int[] coin : coins) {
                q.add(new int[] {top[0] + coin[0], top[1] + coin[1], top[2] + 1});
            }
        }

        return "not possible";
    }
}