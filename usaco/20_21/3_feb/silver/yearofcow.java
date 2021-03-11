/*
Very similar in nature to the Barn Repair problem from the training
portal. For each input year, determine which zodiac cycle it 
belongs to by int-dividing by 12. To avoid needing to write a 
custom comparator, I made the years negative. To make the current 
year belong to cycle 0 (and every other cycle a negative number),
I subtract 12 from that negated year (and THEN divide by 12).

Keep track of all those unique zodiac cycle numbers that pop up.
We can consider the current year as another cycle that we are 
trying to visit, so add that to the set of cycle numbers as well.
Sort them. It will always be optimal to use our first time jump to
go to the earliest cycle, so iterate through the cycle numbers from
the earliest one.

Compare consecutive cycle numbers, and add their difference to a
list. Sort that list. Here greedy works: we will always want to use
one of our time jumps to skip the longest gaps in time. Since we 
use one of our time jumps to get to the earliest zodiac cycle, we
just need the K-1 largest gaps. 

If the earliest zodiac cycle is cycle x, then we know that in the
worst case scenario of K = 1, the answer will be |x*12|. For every
other time jump that we have available to us, subtract that from
|x*12|. This will give us the optimal answer that we are after.
*/

import java.util.*;

public class yearofcow {
    public static int n, k;

    public static void main(String[] args) {
        // Read input, add the cycle number to a set
        // Here I used a sorted set, but you could end up with
        // an ordered list of cycle numbers in some other way
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        k = in.nextInt();
        TreeSet<Integer> groups = new TreeSet<Integer>();
        for (int i = 0; i < n; i++) {
            int y = -in.nextInt();
            groups.add((y - 12) / 12);
        }
        groups.add(0);
        in.close();
        
        // Create a sorted list of the gaps between cycles
        // Note 1: there is no gap between consecutive cycles,
        // since the end of one is the start of the next
        // Note 2: these gaps are positive numbers because we
        // always subtract a smaller number from a larger one
        ArrayList<Integer> jumps = new ArrayList<Integer>();
        int prev = groups.first();
        for (int g : groups) {
            jumps.add(g - prev - 1);
            prev = g;
        }
        Collections.sort(jumps, (a, b) -> { return b - a; });

        // Every zodiac cycle number is a negative number,
        // except for the one that corresponds to the current
        // year. Add back in as many years as possible, being
        // careful to note that we could have more time jumps
        // available to us than there are jumps
        int ans = groups.first();
        for (int i = 0; i < Math.min(k-1, jumps.size()); i++) {
            ans += jumps.get(i);
        }

        // ans now stores a negative number whose absolute value
        // is the number of cycles that we time jump over. The
        // answer is that value times 12.
        System.out.println(ans * -12);
    }
}