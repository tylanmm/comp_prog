import java.io.*;
import java.util.*;

public class nonprimefactors {
    public static ArrayList<Integer> primes = new ArrayList<Integer>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine());
        sieve(1500);

        for (int i = 0; i < q; i++) {
            System.out.println(getFactors(Integer.parseInt(br.readLine())));
        }
    }

    public static void sieve(int n) {
        boolean[] sieve = new boolean[n];
        sieve[0] = sieve[1] = true;
        for (int i = 2; i < n; i++) {
            if (sieve[i]) continue;
            primes.add(i);
            for (int j = i*i; j < n; j += i) sieve[j] = true;
        }
    }

    public static int getFactors(int n) {
        int totalFactors = 1, primeFactors = 0, count = 0;
        int prime = 2, pI = 0; 
        boolean usedPrime = false;
        while (prime*prime <= n) {
            if (n % prime == 0) {
                if (!usedPrime) {
                    usedPrime = true;
                    primeFactors++;
                }
                count++;
                n /= prime;
            } else {
                usedPrime = false;
                totalFactors *= count + 1;
                count = 0;
                prime = primes.get(++pI);
            }
        }
        
        if (n != 1) {
            if (n == prime) {
                totalFactors *= count + 2;
            } else {
                totalFactors *= count + 1;
                primeFactors++;
                totalFactors *= 2;
            }
        }

        return totalFactors - primeFactors;
    }
}