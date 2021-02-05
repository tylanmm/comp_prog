import java.util.*;

public class toys {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt(), k = in.nextInt();
        in.close();

        // update a toy's spot to 1 if it is removed
        BIT toys = new BIT(t);
        
    }
}

// Specifically for range sum queries in a circular array
class BIT {
    private int[] arr;
    private int size;

    public BIT(int n) {
        arr = new int[n];
        size = n;
    }

    public void update(int i, int val) {
        while (i > 0) {
            arr[i] += val;
            i -= i & -i;
        }
    }

    private int rsq(int i) {
        if (i < 0) return 0;
        int total = 0;
        while (i < size) {
            total += arr[i];
            i += i & -i;
        }
        return total;
    }

    public int query(int i, int j) {
        if (i < j) {
            return rsq(j) - rsq(i-1);
        } else {
            // i to end plus beginning to j
            return rsq(size-1) - rsq(i-1) + rsq(j);
        }
    }
}