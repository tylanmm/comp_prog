import java.io.*;

public class where {
    static int n;
    static String[] grid;

    public static void main(String[] args) {
        read();
    }

    public static void read() {
        try (BufferedReader in = new BufferedReader(new File("where.in"))) {
            n = Integer.parseInt(in.readLine().strip());
            grid = new String[n];
            for (int i = 0; i < n; i++) {
                grid[i] = in.readLine().strip();
            }
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}