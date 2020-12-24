import java.util.*;
import java.io.*;

public class rectpasture {
    private static int n;
    private static int[][] points;
    private static int[][] pref;
    
    public static void main(String[] args) {
        ////////////////////
        /* READ THE INPUT */
        ////////////////////
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        points = new int[n][2];
        for (int i = 0; i < n; i++) {
            points[i][0] = in.nextInt();
            points[i][1] = in.nextInt();
        }
        in.close();


        /////////////////////////
        /* COMPRESS THE POINTS */
        /////////////////////////

        // By changing all of the x and y coordinates to be in the rnage 0...n-1,
        // we will be able to use 2D prefix sums to count how many points are in
        // a given range. 
        // This can be done because the x's are distinct, as well as the y's
        
        // Sort by x coordinate
        Arrays.sort(points, (a, b) -> {
            return a[0] - b[0];
        });
        // Re-label x coordinates to 0, 1, 2, ..., n-1
        for (int i = 0; i < n; i++) {
            points[i][0] = i;
        }

        // Sort by y coordinate
        Arrays.sort(points, (a, b) -> {
            return a[1] - b[1];
        });
        // Re-label y coordinates to 0, 1, 2, ..., n-1
        for (int i = 0; i < n; i++) {
            points[i][1] = i;
        }


        //////////////////////////////////
        /* GENERATE 2D PREFIX SUM ARRAY */
        //////////////////////////////////

        // With all points in the range 0...n-1,
        // set each point in the grid to 1
        pref = new int[n][n];
        for (int[] point : points) {
            pref[point[0]][point[1]] = 1;
        }

        // Generate a prefix sum for each row
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n; j++) {
                pref[i][j] += pref[i][j-1];
            }
        }

        // With the row-by-row prefix sums now generated,
        // the column-by-column prefix sums will complete the 2D prefix sum array
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                pref[i][j] += pref[i-1][j];
            }
        }


        ///////////////////////
        /* COUNT THE SUBSETS */
        ///////////////////////

        // The unique subsets of cows will have a cow sitting on each of the four edges.
        
        // If we choose any two points (x1, y2) and (y1, y2) to sit on the top and bottom 
        // edges of the fence, then all of the valid points (x3, y3) to sit on the left 
        // edge would need to satisfy x3 <= min(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2) 
        
        // Similarly, all of the valid points (x4, y4) to sit on the right edge would need
        // to satisfy max(x1, x2) <= x4 and min(y1, y2) <= y4 <= max(y1, y2)

        // To count the number of valid subsets given two points selected as the top and bottom,
        // use the 2D prefix sum array to find the number of valid left points, as well
        // as to find the number of valid right points. The number of subsets given those
        // top and bottom points would be numValidLeft * numValidRight

        // We can start the count at n+1 to account for individual cows and the empty set
        long count = n + 1;

        // For every pair of points
        for (int i = 0; i < n-1; i++) {
            for (int j = i + 1; j < n; j++) {
                // Count the number of valid left points, and the number of valid right points
                // The points were most recently sorted by y, 
                // so points[i][1] < points[j][1]
                int left  = calcPref(0,   Math.min(points[i][0], points[j][0]), points[i][1], points[j][1]);
                int right = calcPref(Math.max(points[i][0], points[j][0]), n-1, points[i][1], points[j][1]);
                count += left * right;
            }
        }

        System.out.println(count);
    }

    // Calculate 2D prefix sum
    // Take the bottom right corner, 
    // subtract the region above and the region to the left,
    // and then add back the top left corner
    private static int calcPref(int loX, int hiX, int loY, int hiY) {
        int whole = pref[hiX][hiY];
        int left = loY > 0 ? pref[hiX][loY - 1] : 0;
        int top = loX > 0 ? pref[loX - 1][hiY] : 0;
        int corner = loX > 0 && loY > 0 ? pref[loX-1][loY-1] : 0;
        return whole - left - top + corner;
    }
}