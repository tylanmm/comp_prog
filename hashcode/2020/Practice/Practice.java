import java.util.Scanner;
import java.io.File;
import java.util.TreeSet;
import java.util.HashMap;
import java.util.ArrayList;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.Writer;
import java.io.IOException;

public class Practice {
    public static HashMap<Integer, Integer> bests = new HashMap<>();
    public static TreeSet<Integer> answer;
    public static int M = 0;

    public static int findMaxSlices(TreeSet<Integer> nums, int sum, TreeSet<Integer> result) {
        Integer bestFit = nums.floor(rem);
        if (bestFit == null || nums.isEmpty()) {
            return sum;
        }
        int with = sum;
        int without = sum;
        if (bestFit + sum < M) {
            nums.remove(bestFit);
            without += findMaxSlice(nums, sum, result);
            result.add(bestFit);
            sum += bestFit;
            with += findMaxSlices(nums, sum, result);
        }
        if (with > without) {
            answer = result;
        }
        else {
            result.remove(bestFit);
            answer = result;
        }
    }
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File(args[0]));
        M = Integer.parseInt(in.next());
        int N = Integer.parseInt(in.next());
        ArrayList<Integer> numsList = new ArrayList<>();
        TreeSet<Integer> nums = new TreeSet<>();
        System.out.println(M);

        for (int i = 0; i < N; i++) {
            int n = Integer.parseInt(in.next());
            numsList.add(n);
            nums.add(n);
        }
        in.close();
        
        TreeSet<Integer> pizzas = new TreeSet<>();
        Integer biggest = nums.floor(M);
        int sum = 0;
        while (biggest != null) {
            sum += biggest;
            pizzas.add(biggest);
            M -= biggest;
            nums.remove(biggest);
            biggest = nums.floor(M);
        }

        Writer out = Files.newBufferedWriter(Paths.get(args[1]));
        out.write(pizzas.size() + "\n");
        for (int p : pizzas) {
            out.write(numsList.indexOf(p) + " ");
        }
        out.close();
        
        System.out.println(sum);
    }
}