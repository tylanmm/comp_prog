import java.util.*;
import java.io.*;

/* 
    At first it looks like a DP problem, but after playing with some test cases,
    you can see that the only valid ways to space the cows in the grid will mean
    that either every row will have alternating cows (ex: C.C., .C.C), or that 
    every column will have alternating cows.

    Examples
    Cows alternating within rows
    C.C.    .C.C    C.C. This last one has
    C.C.    C.C.    .C.C cows alternating
    .C.C    C.C.    C.C. down the columns
    C.C.    .C.C    .C.C as well as across rows

    Cows alternating within columns
    C..C    CC..    .C.C This last one has
    .CC.    ..CC    C.C. cows alternating
    C..C    CC..    .C.C down the columns
    .CC.    ..CC    C.C. as well as across rows

    For each row, separately track the sum of the even-indexed and the odd-indexed elements.
    Do the same thing for each column.

    Keep a running total for the maximum row score by choosing to add either the even-indexed
    sum or the odd-indexed sum. Do the same thing for the maximum column score.

    The result will be the maximum of these two running totals.
*/

public class spaced {
    static int n;
    static int[][] beauty;

    public static void main(String[] args) throws IOException {
        ////////////////////
        // Read the input //
        ////////////////////

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(in.readLine());
        beauty = new int[n][n];

        // store each cell's beauty score
        for (int i = 0; i < n; i++) {
            StringTokenizer line = new StringTokenizer(in.readLine());
            for (int j = 0; j < n; j++) {
                beauty[i][j] = Integer.parseInt(line.nextToken());
            }
        }

        in.close();


        ////////////////////////////////
        // Calculate the running sums //
        ////////////////////////////////

        int rowsTotal = 0;
        int colsTotal = 0;
        for (int i = 0; i < n; i++) {
            int[] rowSums = new int[2];
            int[] colSums = new int[2];

            for (int j = 0; j < n; j++) {
                // the parity of the index determines which total we add to
                rowSums[j % 2] += beauty[i][j];   // (i, j) goes across each row
                colSums[j % 2] += beauty[j][i];   // (j, i) goes down each column
            }

            // keep one of the two sums, whichever is larger
            rowsTotal += Math.max(rowSums[0], rowSums[1]);
            colsTotal += Math.max(colSums[0], colSums[1]);
        }

        System.out.println(Math.max(rowsTotal, colsTotal));
    }
}