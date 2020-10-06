import java.io.*;
import java.util.*;

public class swap {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("swap.in"));
        int n = in.nextInt(), m = in.nextInt(), k = in.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = i;
        
        for (int i = 0; i < m; i++) {
            int s = in.nextInt() - 1;
            int e = in.nextInt() - 1;

            for (int j = 0; j < (e-s+1)/2; j++) {
                int temp = arr[s+j];
                arr[s+j] = arr[e-j];
                arr[e-j] = temp;
            }
        }

        int[] trans = new int[n];
        for (int i = 0; i < n; i++) {
            trans[arr[i]] = i;
        }
        
        System.out.println(Arrays.toString(trans));
        
    }
}
/*
0 1 2 3 4 5 6
0 4 6 5 1 2 3 

0 4 5 6 1 3 2
*/