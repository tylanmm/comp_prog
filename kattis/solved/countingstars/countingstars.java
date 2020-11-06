import java.util.Scanner;

public class countingstars {
    private static int m;
    private static int n;
    private static char[][] grid;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testNum = 1;
        while (in.hasNext()) {
            readGrid(in);
            int amount = solve();
            System.out.printf("Case %d: %d\n", testNum++, amount);
        }
        in.close();
    }

    private static void readGrid(Scanner in) {
        m = in.nextInt();
        n = in.nextInt();
        grid = new char[m][n];
        for (int i = 0; i < m; i++) {
            String line = in.next();
            for (int j = 0; j < n; j++) {
                grid[i][j] = line.charAt(j);
            }
        }
    }

    private static int solve() {
        int amt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '-') {
                    flood(i, j);
                    amt++;
                }
            }
        }
        return amt;
    }

    private static void flood(int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '-') {
            return;
        }

        grid[i][j] = '#';
        flood(i+1, j);
        flood(i, j+1);
        flood(i-1, j);
        flood(i, j-1);
    }
}