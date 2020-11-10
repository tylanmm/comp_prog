import java.util.Scanner;

public class rainbowroadrace {
    public static void main(String[] args) {
        HashMap<Character, Integer> colorMap = new HashMap<Character, Integer>();
        String colors = "ROYGBIV";
        for (int i = 0; i < 7; i++) {
            colorMap.put(colors.charAt(i), 1 << i);
        }

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[][] streets = new int[m][4];
        for (int i = 0; i < m; i++) {
            int l1 = in.nextInt();
            int l2 = in.nextInt();
            int d = in.nextInt();
            int c = colorMap.get(in.next().charAt(0));
            streets[i] = new int[] {l1, l2, d, c};
        }
        in.close();

        int[][][] dp = new int[2*m+1][n+1][2];
        int step = 1;
        while (step < 2*m) {
            for (int[] street : streets) {
                int l1 = street[0];
                int l2 = street[1];
                int d = street[2];
                int c = street[3];
                dp[step][l2][0]
            }
        }
    }
}
