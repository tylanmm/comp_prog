import java.util.*;

class paint {
    static long n;
    static int k;
    static long[][] painters;

    public static void main(String[] args) {
        readInput();

        // sort painters by end time; break ties with increasing start time
        Arrays.sort(painters, (a, b) -> {
            if (a[1] != b[1]) {
                return a[1] > b[1] ? 1 : -1;
            } else {
                return a[0] > b[0] ? 1 : -1;
            }
        });

        System.out.println(n - solve());
    }

    static void readInput() {
        Scanner in = new Scanner(System.in);
        n = in.nextLong();
        k = in.nextInt();
        painters = new long[k][2];
        for (int i = 0; i < k; i++) {
            painters[i][0] = in.nextLong();
            painters[i][1] = in.nextLong();
        }
        in.close();
    }

    static long solve() {
        TreeMap<Long, Long> ends = new TreeMap<Long, Long>();

        long ans = 0;
        for (long[] painter : painters) {
            // find the last painter the current one could follow
            Map.Entry<Long, Long> end = ends.lowerEntry(painter[0]);
            long slats = (end == null ? 0 : end.getValue()) + painter[1] - painter[0] + 1;
            ans = Math.max(ans, slats);

            ends.put(painter[1], ans);
        }

        return ans;
    }
}