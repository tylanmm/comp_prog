import java.io.*;
import java.util.*;

public class ceremony {
    public static void main(String[] args) {
        // read the input
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] buildings = new int[n];
        for (int i = 0; i < n; i++) {
            buildings[i] = in.nextInt();
        }
        in.close();
        Arrays.sort(buildings);

        // greedily remove the best option:
        // either the bottom floor, or the tallest building
        int first = 0, last = n-1, h = 0, steps = 0;
        while (first <= last) {
            while (first <= last && last + 1 <= buildings[last]) {
                steps++;
                last--;
            }

            while (first <= last && last + 1 > buildings[last]) {
                steps++;
                h++;
                while (first <= last && buildings[first] <= h) {
                    first++;
                }
            }
        }

        System.out.println(steps);
    }  
}