import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.io.Writer;
import java.nio.file.Paths;


public class race {
    public static int findTime(int x, int k) {
        int speed = 1;
        int time = 0;
        while (true) {
            k -= speed;
            time++;
            if (k <= 0) {
                return time;
            }
            if (speed >= x) {
                k -= speed;
                time++;
                if (k <= 0) {
                    return time;
                }
            }
            speed++;
        }
    }
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File(args[0]));
        int k = Integer.parseInt(in.next());
        int n = Integer.parseInt(in.next());
        int[] xs = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Integer.parseInt(in.next());
        }
        in.close();

        Writer out = Files.newBufferedWriter(Paths.get(args[1]));
        for (int x : xs) {
            out.write(findTime(x, k));
            out.write("\n");
        }
        out.close();
    }
}