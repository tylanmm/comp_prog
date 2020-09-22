/*
ID: tylan071
LANG: JAVA
TASK: ariprog
*/

import java.io.*;
import java.util.*;

public class ariprog {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("ariprog.in"));
        int n = in.nextInt();
        int m = in.nextInt();
        in.close();
        
        int max = 2 * m * m;
        boolean[] bis = new boolean[max + 1];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= m; j++) {
                bis[i*i + j*j] = true;
            }
        }

        ArrayList<int[]> progs = new ArrayList();
        for (int a = 0; a <= max - n; a++) {
            for (int b = 1; b <= (max-a)/(n-1); b++) {
                boolean isValid = true;
                for (int i = 0; i < n; i++) {
                    if (!bis[a + b*i]) {
                        isValid = false;
                        break;
                    }
                }

                if (isValid) {
                    int[] pair = {a, b};
                    progs.add(pair);
                }
            }
        }

        Collections.sort(progs, new Comparator<int[]>() {
            @Override
            public int compare(int[] p1, int[] p2) {
                if (p1[1] != p2[1]) return p1[1] - p2[1];
                else return p1[0] - p1[0];
            }
        });

        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ariprog.out")));
        for (int[] p : progs) out.println(String.format("%d %d", p[0], p[1]));
	if (progs.size() == 0) out.println("NONE");
        out.close();
    }
}