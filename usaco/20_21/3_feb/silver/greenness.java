import java.util.*;

public class greenness {
    public static int n;
    public static int[][] grid;
    public static int[][][] pref;
    public static HashSet<Box> seen = new HashSet<Box>();

    public static void main(String[] args) {
        // read input, prep 2d prefix sum array
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        grid = new int[n][n];
        pref = new int[n][n][2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int num = in.nextInt();
                grid[i][j] = num < 100 ? 0 : num > 100 ? 2 : 1;
                if (num < 101) {
                    pref[i][j][num < 100 ? 0 : 1] = 1;
                }
            }
        }
        in.close();

        // finish getting prefix sum array ready
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n; j++) {
                for (int k = 0; k < 2; k++) {
                    pref[i][j][k] += pref[i][j-1][k];
                }
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 2; k++) {
                    pref[i][j][k] += pref[i-1][j][k];
                }
            }
        }

        Box b = new Box(0, n-1, n-1, 0);
        System.out.println(numSubgrids(b) - solve(b));
    }

    public static int solve(Box b) {
        if (!b.isGood() || seen.contains(b)) return 0;
        int ans = 0;
        seen.add(b);
        if (contains(b, 1)) {
            if (contains(b, 0)) {
                ans = 1;
                Box b1 = new Box(b);
                b1.left--;
                ans += solve(b1);
                Box b2 = new Box(b);
                b2.top--;
                ans += solve(b2);
                Box b3 = new Box(b);
                b3.right--;
                ans += solve(b3);
                Box b4 = new Box(b);
                b4.bottom--;
                ans += solve(b4);
            }
        } else {
            ans = numSubgrids(b);
        }
        return ans;
    }

    public static boolean contains(Box b, int val) {
        int top = b.top > 0 ? pref[b.top-1][b.right][val] : 0;
        int left = b.left > 0 ? pref[b.bottom][b.left - 1][val] : 0;
        int corner = (b.top > 0 && b.left > 0) ? pref[b.top-1][b.left-1][val] : 0;
        return (pref[b.bottom][b.right][val] - left - top + corner) > 0;
    }

    public static int numSubgrids(Box b) {
        int ver = b.bottom - b.top + 1;
        ver = ver * (ver + 1) / 2;
        int hor = b.right - b.left + 1;
        hor = hor * (hor + 1) / 2;
        return ver * hor;        
    }
}

class Box {
    public int top, right, bottom, left;
    public Box(int top, int right, int bottom, int left) {
        this.top = top;
        this.right = right;
        this.bottom = bottom;
        this.left = left;
    }
    public Box(Box o) {
        this.top = o.top;
        this.right = o.right;
        this.bottom = o.bottom;
        this.left = o.left;
    }
    public boolean isGood() {
        return top <= bottom && left <= right;
    }
    public int hashCode() {
        return Integer.hashCode(top) + Integer.hashCode(right) + Integer.hashCode(bottom) + Integer.hashCode(left);
    }
    public boolean equals(Object other) {
        Box o = (Box) other;
        return top == o.top && right == o.right && bottom == o.bottom && left == o.left;
    }
}