import java.util.*;
import java.io.*;

/*
    After simulating the K swaps, a cow that started at some
    index i will end up at some index j. Similarly, a cow that
    started at index j will end up at some index k. This process
    can repeat and be up to n long.

    If the K-step process moves cow i to index j, and cow j to
    index k, and so on, then i, j, k... are in a cycle, or a
    connected component.

    Determine which component each index belongs to, and then
    step through the K-step process again to see what positions
    the cows of each component pass through.

    After some number of repetitions, every cow in a connected 
    component will pass through the positions that every other
    cow in that connected component pass through.
    
    The size of the visited set for that component (which you
    build during the second pass through the K swaps) is the
    answer for that cow.
*/

public class mooves {
    static int[][] moves;
    static int[] pos;
    static int[] comp;
    static HashSet<Integer>[] visits;
    
    public static void main(String[] args) throws IOException {
        ////////////////////
        // Read the input //
        ////////////////////

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] line = in.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int k = Integer.parseInt(line[1]);


        ///////////////////////////////////////
        // Step through the swapping process //
        ///////////////////////////////////////

        // keeps track of the current ordering
        pos = new int[n];
        for (int i = 0; i < n; i++) {
            pos[i] = i;
        }

        moves = new int[k][2];
        for (int i = 0; i < k; i++) {
            // read the indices to be swapped
            line = in.readLine().split(" ");
            int a = Integer.parseInt(line[0]) - 1;
            int b = Integer.parseInt(line[1]) - 1;

            // store the swap info
            moves[i][0] = a;
            moves[i][1] = b;
            
            // swap the cows
            int temp = pos[a];
            pos[a] = pos[b];
            pos[b] = temp;
        }

        in.close();


        //////////////////////////////
        // Determine the components //
        //////////////////////////////
        
        comp = new int[n];
        int compnum = 0;
        for (int i = 0; i < n; i++) {
            if (comp[i] == 0) {
                dfs(i, ++compnum);
            }
        }
        

        /////////////////////////////////////////////
        // Step through the swapping process again //
        /////////////////////////////////////////////
        
        // tracks which positions are visited by cows in component i
        visits = new HashSet[compnum+1];
        for (int i = 0; i < compnum+1; i++) {
            visits[i] = new HashSet<Integer>();
        }

        // step through the swapping proces again
        for (int[] swap : moves) {
            // put a into the set of visited indices for the component of the cow at pos[a]
            // same thing for b
            int a = swap[0], b = swap[1];
            visits[comp[pos[a]]].add(a);
            visits[comp[pos[b]]].add(b);

            // swap them
            int temp = pos[a];
            pos[a] = pos[b];
            pos[b] = temp;
        }


        ////////////////////////////////////////
        // Output the number of visited spots //
        ////////////////////////////////////////
        
        // for every cow, the answer is the size of the visited set for that cow's component
        // if a cow is alone in its component, then the answer is just 1
        for (int i = 0; i < n; i++) {
            if (visits[comp[i]].size() == 0){
                System.out.println(1);
            } else {
                System.out.println(visits[comp[i]].size());
            }
        }
    }

    // simple dfs; rather than just mark as visited, assign cows to components
    public static void dfs(int cow, int compnum) {
        comp[cow] = compnum;
        if (comp[pos[cow]] == 0) {
            dfs(pos[cow], compnum);
        }
    }
}