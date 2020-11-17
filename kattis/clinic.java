import java.io.*;
import java.util.*;

public class clinic {
    private static int n, k, time;
    private static PriorityQueue<Patient> pq;
    private static HashSet<String> skip;
    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader();
        n = in.nextInt();
        k = in.nextInt();
        pq = new PriorityQueue<Patient>();
        skip = new HashSet<String>();
        for (int i = 0; i < n; i++) {
            processQuery(in);
        }
    }

    private static void processQuery(FastReader in) throws IOException {
        int q = in.nextInt();
        time = in.nextInt();
        if (q == 1) {
            String m = in.next();
            int s = in.nextInt();
            pq.add(new Patient(time, s, m));
        } 
        
        else if (q == 2) {
            if (pq.isEmpty()) {
                System.out.println("doctor takes a break");
                return;
            }

            Patient p = pq.poll();
            while (!pq.isEmpty() && skip.contains(p.m)) {
                p = pq.poll();
            }

            if (!pq.isEmpty() || !skip.contains(p.m)) {
                System.out.println(p.m);
            } else {
                System.out.println("doctor takes a break");
            }
        } 
        
        else {
            skip.add(in.next());
        }
    }

    static class Patient implements Comparable<Patient> {
        public int t;
        public int s;
        public String m;
    
        public Patient(int t, int s, String m) {
            this.t = t;
            this.s = s;
            this.m = m;
        }
    
        public int compareTo(Patient o) {
            int val1 = s + k*(time - t);
            int val2 = o.s + k*(time - o.t);
            if (val1 != val2) {
                return val2 - val1;
            }
            return m.compareTo(o.m);
        }
    }
}

class FastReader {
    private BufferedReader in;
    private String[] line = new String[0];
    private int pos = 0;

    public FastReader() throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
    }

    public void close() throws IOException {
        in.close();
    }

    public String[] nextLine() throws IOException {
        line = in.readLine().split(" ");
        return line;
    }

    public String next() throws IOException {
        while (pos == line.length) {
            nextLine();
            pos = 0;
        }

        return line[pos++];
    }

    public int nextInt() throws IOException {
        String val = next();
        return Integer.parseInt(val);
    }
}