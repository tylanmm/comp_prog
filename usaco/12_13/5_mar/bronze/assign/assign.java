import java.util.*;
import java.io.*;

public class assign {
    private static int n;
    private static int k;
    private static int[][] rules;
    
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new BufferedReader(new FileReader("assign.in")));
        n = in.nextInt();
        k = in.nextInt();
        rules = new int[k][3];
        for (int i = 0; i < k; i++) {
            rules[i][0] = in.next().charAt(0) == 'S' ? 1 : 0;
            rules[i][1] = in.nextInt() - 1;
            rules[i][2] = in.nextInt() - 1;
        }
        in.close();
        
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("assign.out")));
        out.println(countValidAssignments(new int[n], 0));
        out.close();
    }

    private static int countValidAssignments(int[] assignments, int pos) {
        if (pos == n) {
            return isValid(assignments);
        }

        int total = 0;
        for (int i = 0; i < 3; i++) {
            assignments[pos] = i;
            total += countValidAssignments(assignments, pos+1);
        }
        return total;
    }

    private static int isValid(int[] assignments) {
        for (int i = 0; i < k; i++) {
            if (rules[i][0] == 1) {
                if (assignments[rules[i][1]] != assignments[rules[i][2]]) {
                    return 0;
                }
            } else {
                if (assignments[rules[i][1]] == assignments[rules[i][2]]) {
                    return 0;
                }
            }
        }
        return 1;
    }
}