import java.util.Scanner;
public class drivinglanes {
    private static int[] length;
    private static int[][] curve;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int k = in.nextInt();
        int r = in.nextInt();

        // read straightaways
        length = new int[n];
        for (int i = 0; i < n; i++) {
            length[i] = in.nextInt();
        }

        // read curves
        curve = new int[n-1][2];
        for (int i = 0; i < n-1; i++) {
            curve[i][0] = in.nextInt();
            curve[i][1] = in.nextInt();
        }

        in.close();

        int bestLane = curve[n-2][1] >= 0 ? 0 : m-1;

        int[][] dp = new int[n][m];
        for (int i = n-2; i > -1; i--) {
            int nextBest = 0;
            for (int j = 0; j < m; j++) {
                if (Math.abs(j - bestLane) * k <= length[i]) {
                    
                }
            }
        }
    }
}
