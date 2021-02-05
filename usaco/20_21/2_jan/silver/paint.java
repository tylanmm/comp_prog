import java.util.*;
import java.io.*;

/*
    We basically need to know how many disconnected strips
    of each color are necessary on either side of the unpainted
    region. A strip of paint can span the entire fence unless
    there is a lighter color that appears after the darker
    color appears for the first time and before the darker
    color appears for the last time.

    int[][] left keeps track of the total number of disconnected
    strips up until index i, and int[][] right keeps track of
    the total number of disconnected strips after index i.
    
    With these arrays, the answer to the query (a, b) is given
    by adding left[a-1] and right[b+1] to some running total.

    Note: this is NOT an optimized solution: it is long and
    messy, and it times out on test cases 12 and 13 (it passes
    all of the others, however). Once the problems are posted,
    I will come back and optimize this solution more.
*/

public class paint {
    static int n;
    static int q;
    static int[][] left;
    static int[][] right;

    public static void main(String[] args) {
        //////////////////
        // Read in data //
        //////////////////

        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        q = in.nextInt();
        String fence = in.next();

        
        /////////////////////////////
        // Preprocess fence colors //
        /////////////////////////////

        // Count the number of unique paint strips from left to right
        int count = 0;
        ArrayList<Character> stack = new ArrayList<Character>();
        int[] fromLeft = new int[n];
        for (int i = 0; i < n; i++) {
            // End all strips that are darker than the current one
            char currColor = fence.charAt(i);
            while (!stack.isEmpty() && stack.get(stack.size()-1) > currColor) {
                stack.remove(stack.size()-1);
            }

            // Any time we see a darker color, it's a new strip
            if (stack.isEmpty() || stack.get(stack.size()-1) < currColor) {
                count++;
            }

            stack.add(currColor);
            fromLeft[i] = count;
        }

        // Count the number of unique paint strips from right to left
        stack.clear();
        count = 0;
        int[] fromRight = new int[n];
        for (int i = n-1; i >= 0; i--) {
            // End all strips that are darker than the current one
            char currColor = fence.charAt(i);
            while (!stack.isEmpty() && stack.get(stack.size()-1) > currColor) {
                stack.remove(stack.size()-1);
            }

            // Any time we see a darker color, it's a new strip
            if (stack.isEmpty() || stack.get(stack.size()-1) < currColor) {
                count++;
            }

            stack.add(currColor);
            fromRight[i] = count;
        }


        ////////////////////
        // Answer queries //
        ////////////////////

        // to respond to a query, add the amount of distinct strips to the left and right
        for (int i = 0; i < q; i++) {
            int a = in.nextInt() - 1;
            int b = in.nextInt() - 1;
            int res = 0;
            
            res += a > 0 ? fromLeft[a-1] : 0;
            res += b < n-1 ? fromRight[b+1] : 0;
            
            System.out.println(res);
        }

        in.close();
    }
}