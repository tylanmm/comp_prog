import java.io.*;
import java.util.*;

public class cownomics {
    static int[][] spotty;
    static int[][] plain;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new FileReader("cownomics.in"));
        String[] nums = in.readLine().split(" ");
        N = Integer.parseInt(nums[0]);
        M = Integer.parseInt(nums[1]);

        spotty = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = in.readLine();
            for (int j = 0; j < M; j++) {
                char c = line.charAt(j);
                spotty[i][j] = c == 'A' ? 1 : c == 'C' ? 2 : c == 'G' ? 3 : 4;
            }
        }

        plain = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = in.readLine();
            for (int j = 0; j < M; j++) {
                char c = line.charAt(j);
                plain[i][j] = c == 'A' ? 1 : c == 'C' ? 2 : c == 'G' ? 3 : 4;
            }
        }

        in.close();

        int count = 0;
        for (int i = 0; i < M - 2; i++) {
            for (int j = i + 1; j < M - 1; j++) {
                for (int k = j + 1; k < M; k++) {
                    count += checkGroup(i, j, k) ? 1 : 0;
                }
            }
        }

        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("cownomics.out")));
        out.println(count);
        out.close();
    }

    static boolean checkGroup(int i, int j, int k) {
        HashSet<Integer> nums = new HashSet<Integer>(N);
        for (int[] cow : spotty) {
            nums.add(16*cow[i] + 4*cow[j] + cow[k]);
        }

        for (int[] cow : plain) {
            if (nums.contains(16*cow[i] + 4*cow[j] + cow[k])) {
                return false;
            }
        }
        return true;
    }
}
