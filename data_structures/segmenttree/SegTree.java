// Currently set up to find range sums
// Modify the lines commented with "ADJUST FOR OTHER OPS" for other operations
// Additionally, modify line commented with "ADJUST BASE FOR OTHER OPS" with
// the value that should be used when returning from an excluded interval
public class SegTree {
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
            t[i] = t[2*i] + t[2*i+1]; // ADJUST FOR OTHER OPS
        }
    }

    private _q(int node, int nL, int nR, int qL, int qR) {
        // if the node is completely in the query range, return its value
        if (qL <= nL && nR <= qR) {
            return t[node];
        }
        // if the node is completely out of the query range, return 0
        if (nR < qL || qR < nL) {
            return 0; // ADJUST BASE FOR OTHER OPS
        }

        // go down into left and right children
        int mid = (nL + nR) / 2;
        return _q(node*2, nL, mid, qL, qR) + _q(node*2+1, mid+1, nR, qL, qR); // ADJUST FOR OTHER OPS
    }

    public query(int left, int right) {
        return _q(1, 0, n-1, left, right);
    }

    public update(int i, int val) {
        // update, and then propogate the change upwards
        t[n+i] = val;
        for (int j = (n+1)/2; j > 0; j /= 2) {
            t[j] = t[j*2] + t[j*2+1]; // ADJUST FOR OTHER OPS
        }
    }
}