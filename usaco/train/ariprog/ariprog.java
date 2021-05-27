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
	HashSet<Integer> bs = new HashSet<Integer>();
        for (int i = 0; i <= m; i++) {
            for (int j = i; j <= m; j++) {
		int b = i*i + j*j;
                bis[b] = true;
		bs.add(b);
            }
        }

        ArrayList<int[]> progs = new ArrayList();
        for (int a : bs) {
	    int cap = (max - a) / (n - 1);
            for (int b = 1; b <= cap; b++) {
                boolean isValid = true;
                for (int i = 0; i < n; i++) {
                    if (!bis[a + b*i]) {
                        isValid = false;
                        break;
                    }
                }

                if (isValid) progs.add(new int[] {a, b});
            }
        }

        Collections.sort(progs, (a, b) -> {
            return (a[1] != b[1]) ? a[1] - b[1] : a[0] - b[0];
        });

        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ariprog.out")));
        for (int[] p : progs) out.println(String.format("%d %d", p[0], p[1]));
	if (progs.isEmpty()) out.println("NONE");
        out.close();
    }
}