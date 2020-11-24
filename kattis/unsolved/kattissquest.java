import java.io.*;
import java.util.*;

public class template {
    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader();
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {

        }
    }

    private static void processCommand(FastReader in) {
        String comm = in.next();
        if (comm.equals("add")) {
            int e = in.nextInt();
            int g = in.nextInt();
        }
    }
}

class FastReader {
    private BufferedReader in;
    private String[] line;
    private int pos = 0;

    public FastReader() throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
    }

    public String[] nextLine() throws IOException {
        line = in.nextLine().split(" ");
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