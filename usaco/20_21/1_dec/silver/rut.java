import java.util.*;
import java.io.*;

/*
    Need to look at every pair of cows (that's why there are only 1000)
    Determine if they intersect (x of the N/S cow, y of the E/W cow, etc.)
    Whichever cow is farther from that point is the one that would be stopped
    Track the closest point and the causer
    Run DFS/BFS on the resulting forest
    Start from cows that didn't cause anything

    . | . . . E x > > > > > >
    . | . . E > + > > > > > >
    . | . . . . ^ . . . . E x
    . | . . . . N . . . . . ^
    . | . . . . . . . . E > x
    . | . . . . . . . . . . N
    --+----------------------
    . | . . . . . . . . . . .
*/

public class rut {
    private static int n;
    private static int[][] cow;
    private static int[] parent;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        cow = new int[n+1][3];
        for (int i = 1; i <= n; i++) {
            char dir = in.next().charAt(0);
            cow[i][0] = dir == 'E' ? 0 : dir == 'N' ? 2 : dir == 'W' ? 1 : 3;
            cow[i][1] = in.nextInt();
            cow[i][2] = in.nextInt();
        }
        in.close();

        findParents();

    }  

    private static void findParents() {
        parent = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = findParent(i);
        }
        System.out.println(Arrays.toString(parent));
    }

    private static int findParent(int c) {
        int p = 0, d = (int) (2e31 - 1);
        for (int i = 1; i <= n; i++) {
            if (i == c) continue;

            // going opposite directions
            if ((cow[c][0] ^ 1) == cow[i][0]) {
                // E/W, same y coordinate
                if (cow[c][0] <= 1 && cow[c][2] == cow[i][2]) {
                    int thisDist = (cow[c][1] + cow[i][1])/2 + 1;
                    if (thisDist < d) {
                        d = thisDist;
                        p = i;
                    }
                } 
                // N/S, same x coordinate
                else if (cow[c][0] >= 2 && cow[c][1] == cow[i][1]) {
                    int thisDist = (cow[c][2] + cow[c][2])/2 + 1;
                    if (thisDist < d) {
                        d = thisDist;
                        p = i;
                    }
                }
            } 
            
            // going the same direction
            else if (cow[c][0] == cow[i][0]) {
                // E/W, same y coordinate
                if (cow[c][0] <= 1 && cow[c][2] == cow[i][2]) {
                    // cow[c] is going east, cow[i] is farther east, and the distance is less
                    if (cow[c][0] == 0 && cow[c][1] < cow[i][1] && cow[i][1] - cow[c][1] < d) {
                        d = cow[i][1] - cow[c][1];
                        p = i;
                    } 
                    // cow[c] is going west, cow[i] is farther west, and the distance is less
                    else if (cow[i][1] < cow[c][1] && cow[c][1] - cow[i][1] < d) {
                        d = cow[c][1] - cow[i][1];
                        p = i;
                    }
                }

                // N/S, same x coordinate
                else if (cow[c][0] >= 2 && cow[c][1] == cow[i][1]) {
                    // cow[c] is going north, cow[i] is farther north, and the distance is less
                    if (cow[c][0] == 2 && cow[c][2] < cow[i][2] && cow[i][2] - cow[c][2] < d) {
                        d = cow[i][2] - cow[c][2];
                        p = i;
                    } 
                    // cow[c] is going south, cow[i] is farther south, and the distance is less
                    else if (cow[i][2] < cow[c][2] && cow[c][2] - cow[i][2] < d) {
                        d = cow[c][2] - cow[i][2];
                        p = i;
                    }
                }
            }

            // going in perpendicular directions
            else {
                int[] inter = intersection(c, i);
                if (inter != null) {
                    int thisDist = dist(c, inter);
                    int otherDist = dist(i, inter);
                    if (thisDist > otherDist && thisDist < d) {
                        d = thisDist;
                        p = i;
                    }
                }
            }
        }

        return p;
    }

    // If two perpendicular cow's will cross paths, return those paths
    private static int[] intersection(int c1, int c2) {
        int[] inter = null;
        if (cow[c1][0] == 0) {
            if (cow[c2][0] == 2 && cow[c1][1] <= cow[c2][1] && cow[c1][2] >= cow[c2][2]) {
                inter = new int[] {cow[c1][1], cow[c2][2]};
            } else if (cow[c2][0] == 3 && cow[c1][1] <= cow[c2][1] && cow[c1][2] <= cow[c2][2]) {
                inter = new int[] {cow[c1][1], cow[c2][2]};
            }
        } else if (cow[c1][0] == 1) {
            if (cow[c2][0] == 3 && cow[c1][1] >= cow[c2][1] && cow[c1][2] >= cow[c2][2]) {
                inter = new int[] {cow[c1][1], cow[c2][2]};
            } else if (cow[c2][0] == 2 && cow[c1][1] >= cow[c2][1] && cow[c1][2] <= cow[c2][2]) {
                inter = new int[] {cow[c1][1], cow[c2][2]};
            }
        } else if (cow[c1][0] == 2) {
            if (cow[c1][0] == 0 && cow[c2][1] <= cow[c1][1] && cow[c2][2] >= cow[c1][2]) {
                inter = new int[] {cow[c2][1], cow[c1][2]};
            } else if (cow[c1][0] == 1 && cow[c2][1] <= cow[c1][1] && cow[c2][2] <= cow[c1][2]) {
                inter = new int[] {cow[c2][1], cow[c1][2]};
            }
        } else {
            if (cow[c1][0] == 1 && cow[c2][1] <= cow[c1][1] && cow[c2][2] >= cow[c1][2]) {
                inter = new int[] {cow[c2][1], cow[c1][2]};
            } else if (cow[c1][0] == 0 && cow[c1][1] <= cow[c1][1] && cow[c2][2] <= cow[c1][2]) {
                inter = new int[] {cow[c2][1], cow[c1][2]};
            }
        }
        return inter;
    }

    private static int dist(int c, int[] loc) {
        return Math.abs(loc[0] - cow[c][1]) + Math.abs(loc[1] - cow[c][2]);
    }
}