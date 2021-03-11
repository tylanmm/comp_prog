/*
Represent the grid with two 2D int arrays. One keeps track
of whether a cow is in that cell, the other counts how many 
neighbors a given cell has. In this version of the problem, 
FJ will always add a cow to make a cow, that would
otherwise be comfortable, uncomfortable.

Differentiate between two different kinds of cows: cows that
simply added, and cows that are added to make cows 
uncomfortable. The latter kind can always be replaced by
the first kind if a specific location calls for it.

Place a cow. If there is a "phantom" cow there (one that can
be overwritten), then decrease the count of phantom cows and
overwrite that cell in grid with a 1 (or whatever you use to
represent "real" cows). Increment the neighbor count of each
neighboring cell, and then check to see if that increase
resulted in that neighbor becoming comfortable.

If a neighbor just became comfortable, then place a phantom
cow in the only open cell around it. This process could
start a chain reaction, so this update/check sequence is
done recursively.

Because cows are only ever added and never removed, and 
because the comfortable "threshold" is exactly three, we 
never have to worry about removing any of the phantom cows,
just replacing them.

Note: because of how the addition of phantom cows and grow,
we could end up going outside of the originally specified
1001x1001 grid. To handle this, shift every coordinate up &
to the right by 502, since the most that a chain reaction of
phantom cows could grow out is 501 (imagine a wall of cows
that is 1001 tall and 2 wide). Because of this choice, you
never have to worry about going out of bounds.
*/

import java.util.*;

public class comfortable {
    public static int n;
    public static int count = 0;
    public static int[][] grid = new int[2005][2005];
    public static int[][] neighbors = new int[2005][2005];

    public static void main(String[] args) {
        // Read in data, call recursive method, print answer
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        for (int i = 0; i < n; i++) {
            int x = in.nextInt() + 502, y = in.nextInt() + 502;
            addCow(x, y, 1);
            System.out.println(count);
        }
        in.close();
    }

    public static void addCow(int x, int y, int type) {
        // If there is a phantom cow here, just replace it
        if (grid[x][y] == 2) {
            if (type == 1) count--;
        } else if (grid[x][y] == 0) {
            // If we are in this method because of a phantom cow,
            // be sure to increase that counter
            if (type == 2) count++;
            grid[x][y] = type;

            // Increment the neighbor count for adjacent cells
            neighbors[x-1][y]++;
            neighbors[x+1][y]++;
            neighbors[x][y-1]++;
            neighbors[x][y+1]++;

            // Check every adjacent cell (including self) to
            // see if they are now comfortable
            check(x, y);
            check(x-1, y);
            check(x+1, y);
            check(x, y-1);
            check(x, y+1);
        }
    }

    public static void check(int x, int y) {
        // If there's actually a cow in this cell
        // and this cow is currently comfortable
        if (grid[x][y] != 0 && neighbors[x][y] == 3) {
            if (grid[x-1][y] == 0) addCow(x-1, y, 2);
            if (grid[x+1][y] == 0) addCow(x+1, y, 2);
            if (grid[x][y-1] == 0) addCow(x, y-1, 2);
            if (grid[x][y+1] == 0) addCow(x, y+1, 2);
        }
    }
}