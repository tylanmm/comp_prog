package pizza;

import java.util.Scanner;
import java.io.File;
import java.util.TreeSet;
import java.util.ArrayList;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.Writer;
import java.io.IOException;

public class Practice {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File(args[0]));
        int M = Integer.parseInt(in.next());
        int N = Integer.parseInt(in.next());
        ArrayList<Integer> numsList = new ArrayList<>();
        TreeSet<Integer> nums = new TreeSet<>();

        for (int i = 0; i < N; i++) {
            nums.add(Integer.parseInt(in.next()));
        }
        in.close();
        
        TreeSet<Integer> pizzas = new TreeSet<>();
        Integer biggest = nums.floor(M);
        while (biggest != null) {
            pizzas.add(biggest);
            M -= biggest;
            nums.remove(biggest);
            biggest = nums.floor(M);
        }

        Writer out = Files.newBufferedWriter(Paths.get(args[1]));
        out.write(pizzas.size());
        for (int p : pizzas) {
            out.write(numsList.indexOf(p));
            out.write(" ");
        }
    }
}