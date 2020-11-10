import java.io.*;
import java.util.*;

public class drivinglanes {
    public static void main(String[] args) throws IOException {
        // read in the data
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] line = in.readLine().split(" ");
        int n = Integer.parseInt(line[0]), m = Integer.parseInt(line[1]);
        line = in.readLine().split(" ");
        int k = Integer.parseInt(line[0]), r = Integer.parseInt(line[1]); 

        int[] straight = new int[n];
        for (int i = 0; i < n; i++) {
            straight[i] = Integer.parseInt(in.readLine());
        }

        int[][] curve = new int[n-1][2];
        for (int i = 0; i < n-1; i++) {
            line = in.readLine().split(" ");
            curve[i][0] = Integer.parseInt(line[0]);
            curve[i][1] = Integer.parseInt(line[1]);
        }
        
        // process first segment (since it isn't dependent upon a previous segment)
        int[][] dp = new int[n][m];
        for (int lane = 0; lane < m; lane++) {
            if (lane*k <= straight[0]) {
                dp[0][lane] = straight[0] + lane*r + (n > 1 ? curve[0][0] + curve[0][1]*(lane+1) : 0);
            } else {
                break;
            }
        }
        
        for (int seg = 1; seg < n-1; seg++) {
            for (int lane = 0; lane < m; lane++) {
                // for each lane, figure out what the best previous lane was
                int minDist = 2000000000, minLane = -1;
                for (int prevLane = 0; prevLane < m; prevLane++) {
                    if ((dp[seg-1][prevLane] != 0) && (Math.abs(lane - prevLane)*k <= straight[seg])) {
                        if (dp[seg-1][prevLane] < minDist) {
                            minDist = dp[seg-1][prevLane];
                            minLane = prevLane;
                        }
                    }
                }
                // distance = best previous distance + this segment's length + r*numLaneChanges + next curve length
                dp[seg][lane] = minLane == -1 ? 0 : minDist + straight[seg] + Math.abs(minLane - lane)*r + curve[seg][0] + curve[seg][1]*(lane+1);
            }
        }

        System.out.println(n > 1 ? dp[n-2][0] + straight[n-1] : dp[0][0]);
    }
}