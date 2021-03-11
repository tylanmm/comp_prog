import java.io.*;
import java.util.*;

public class nonprimefactors {
    private static int[] numFactors = new int[2000001];
    private static HashMap<Integer, Integer>[] primeFactors = new HashMap[2000001];

    public static void main(String[] args) throws IOException {
        sieve();
        numFactors[1] = 1;
        primeFactors[1] = new HashMap<Integer, Integer>();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(in.readLine());
        for (int i = 0; i < q; i++) {
            int n = Integer.parseInt(in.readLine());
            System.out.println(nonprimeFactors(n));
        }
        in.close();
    }

    private static void sieve() {
        for (int i = 2; i < 2000001; i++) {
            if (primeFactors[i] != null) continue;
            primeFactors[i] = new HashMap<Integer, Integer>();
            primeFactors[i].put(i, 1);
            numFactors[i] = 2;
            for (long j = i; j < 2000001L; j += i) {
                if (primeFactors[(int)j] == null) primeFactors[(int)j] = new HashMap<Integer, Integer>();
                primeFactors[(int)j].put(i, 1);
            }
        }
    }

    private static int nonprimeFactors(int n) {
        if (numFactors[n] != 0) {
            return numFactors[n] - primeFactors[n].size();
        }

        for (int prime : primeFactors[n].keySet()) {
            int factor = n / prime;
            nonprimeFactors(factor);
            if (primeFactors[n].get(prime) == 1) {
                numFactors[n] = numFactors[factor] * 2;
            } else {
                numFactors[n] = numFactors[factor];
            }
        }

        return numFactors[n];
    }
}