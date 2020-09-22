import java.io.*;

public class tildes {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] line = in.readLine().split(" ");
        int n = Integer.parseInt(line[0]), q = Integer.parseInt(line[1]);
        UFDS groups = new UFDS(n+1);

        for (int i = 0; i < q; i++) {
            line = in.readLine().split(" ");
            if (line[0].equals("t")) {
                int a = Integer.parseInt(line[1]), b = Integer.parseInt(line[2]);
                groups.union(a, b);
            } else {
                int a = Integer.parseInt(line[1]);
                System.out.println(groups.groupSize(a));
            }
        }

        in.close();
    }
}

class UFDS {
    private int[] parent;
    private int[] rank;
    private int[] size;

    public UFDS(int n) {
        parent = new int[n];
        rank = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int findSet(int i) {
        if (parent[i] == i) return i;
        parent[i] = findSet(parent[i]);
        return parent[i];
    }

    public void union(int i, int j) {
        int x = findSet(i), y = findSet(j);
        if (x != y) {
            if (rank[x] < rank[y]) {
                parent[x] = y;
                size[y] += size[x];
            } else {
                parent[y] = x;
                size[x] += size[y];
                rank[x] += rank[x] == rank[y] ? 1 : 0;
            }
        }
    }

    public int groupSize(int i) {
        return size[findSet(i)];
    }
}