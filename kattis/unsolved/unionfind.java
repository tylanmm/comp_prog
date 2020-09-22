import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class unionfind {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        UFDS sets = new UFDS(n);
        
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(in.readLine());
            String op = st.nextToken();
            int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
            if (op.equals("=")) sets.union(a, b);
            else System.out.println(sets.sameSet(a, b) ? "yes" : "no");
        }
    }
}

class UFDS {
    private int[] parent;
    private int[] rank;

    public UFDS(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int findSet(int i) {
        if (parent[i] == i) return i;
        int result = findSet(parent[i]);
        parent[i] = result;
        return result;
    }

    public boolean sameSet(int i, int j) {
        return findSet(i) == findSet(j);
    }

    public void union(int i, int j) {
        int x = findSet(i), y = findSet(j);
        if (x != y) {
            if (rank[x] < rank[y]) {
                parent[x] = y;
            } else if (rank[y] < rank[x]) {
                parent[y] = x;
            } else {
                parent[x] = y;
                rank[x]++;
            }
        }
    }
}