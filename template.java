import java.io.*;
import java.util.*;

public class template {
    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader();
        
    }
}

class FastReader {
    private BufferedReader in;
    private StringTokenizer line;

    public FastReader() throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
    }

    public void close() throws IOException {
        in.close();
    }

    public String nextLine() throws IOException {
        return in.readLine();
    }

    private void buffer() throws IOException {
        if (line == null || !line.hasMoreTokens()) {
            line = new StringTokenizer(in.readLine());
        }
    }

    public String next() throws IOException {
        buffer();
        return line.nextToken();
    }

    public int nextInt() throws IOException {
        String val = next();
        return Integer.parseInt(val);
    }
}