import java.io.*;
import java.util.*;

public class worstweather {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int n, m;

        do {
            n = Integer.parseInt(in.readLine());
            int[] year = new int[n];
            int[] rain = new int[n];
            for (int i = 0; i < n; i++) {
                String[] line = in.readLine().split(" ");
                year[i] = Integer.parseInt(line[0]);
                rain[i] = Integer.parseInt(line[1]);
            }

            SegTree tree = new SegTree(rain);
            m = Integer.parseInt(in.readLine());
            for (int i = 0; i < m; i++) {
                String[] line = in.readLine().split(" ");
                int loY = Integer.parseInt(line[0]);
                int hiY = Integer.parseInt(line[1]);
                int lo = Arrays.binarySearch(year, loY);
                int hi = Arrays.binarySearch(year, hiY);
                String res = "false";

                if (lo >= 0 && hi >= 0) {

                } else if (lo < 0) {
                    
                }

                // data for query years exist
                if (hi >= 0 && lo >= 0) {
                    // later year <= the earlier
                    if (rain[hi] <= rain[lo]) {
                        // at least one year between them
                        if (hi - lo > 1) {
                            int max = tree.query(lo+1, hi-1);
                            // internal years are all lower than later year
                            if (max < rain[hi]) {
                                // data for all years exist
                                if (hi - lo == hiY - loY) {
                                    res = "true";
                                } else {
                                    res = "maybe";
                                }
                            }
                        } else {
                            res = "true";
                        }
                    }
                } else if (hi < 0) {
                    res = "maybe";
                } else {
                    lo = -lo - 1;
                    int max = tree.query(lo, hi-1);
                    // internal years are all lower than later year
                    if (lo == hi || max < rain[hi]) {
                        res = "maybe";
                    }
                }

                out.write(res);
                out.write("\n");
            }

            out.write("\n");
            in.readLine();

        } while (n != 0 && m != 0);

        in.close();
        out.close();
    }
}

class SegTree {
    private int n;
    private int[] t;

    public SegTree(int[] nums) {
        // find size of complete binary tree
        int n = nums.length;
        this.n = n;
        int lsb = n & -n;
        while (lsb != n) {
            n += lsb;
            lsb = n & -n;
        }

        // pad the tree
        t = new int[2*n];
        for (int i = 0; i < this.n; i++) {
            t[n+i] = nums[i];
        }

        // propogate the values
        for (int i = n-1; i > 0; i--) {
            t[i] = Math.max(t[2*i], t[2*i+1]);
        }
    }

    private int _q(int node, int nL, int nR, int qL, int qR) {
        // if the node is completely in the query range, return its value
        if (qL <= nL && nR <= qR) {
            return t[node];
        }
        // if the node is completely out of the query range, return 0
        if (nR < qL || qR < nL) {
            return 0;
        }

        // go down into left and right children
        int mid = (nL + nR) / 2;
        return Math.max(_q(node*2, nL, mid, qL, qR), _q(node*2+1, mid+1, nR, qL, qR));
    }

    public int query(int left, int right) {
        return _q(1, 0, n-1, left, right);
    }

    public void update(int i, int val) {
        // update, and then propogate the change upwards
        t[n+i] = val;
        for (int j = (n+1)/2; j > 0; j /= 2) {
            t[j] = Math.max(t[j*2], t[j*2+1]);
        }
    }
}