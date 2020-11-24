import java.util.Scanner;
import java.io.*;

public class race {
    public static int findTime(int x, int k) {
        int speed = 1;
        int time = 0;
        while (true) {
            // take off distance while speeding up
            k -= speed;
            time++;
            if (k <= 0) {
                return time;
            }
            
            // take off distance while slowing down
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
        Scanner in = new Scanner(new File("race.in"));
        int k = Integer.parseInt(in.next());
        int n = Integer.parseInt(in.next());
        int[] xs = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Integer.parseInt(in.next());
        }
        in.close();

        BufferedWriter bw = new BufferedWriter(new FileWriter("race.out"));
        for (int x : xs) {
            bw.write(Integer.toString(findTime(x, k)));
            bw.write("\n");
        }
        bw.close();
    }
}