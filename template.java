import java.io.*;
import java.util.*;

public class template {
    public static void main(String[] args) throws IOException {

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
        pos = 0;
        return line;
    }

    public String next() throws IOException {
        while (pos == line.length) {
            nextLine();
        }

        return line[pos++];
    }

    public int nextInt() throws IOException {
        String val = next();
        return Integer.parseInt(val);
    }
}