import java.io.*;
import java.util.HashSet;

public class boggle {
    private static int[] points = {0, 0, 0, 1, 1, 2, 3, 5, 11};
    private static HashSet<String> words;
    private static String[] grid = new String[4];
    private static boolean[][] visited;

    public static void main(String args[]) throws IOException {
        // read in valid words
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int w = Integer.parseInt(in.readLine());
        words = new HashSet<String>(w);
        for (int i = 0; i < w; i++) {
            words.add(in.readLine());
        }

        in.readLine();
        int b = Integer.parseInt(in.readLine());
        for (int i = 0; i < b; i++) {
            for (int j = 0; j < 4; j++) {
                grid[j] = in.readLine();
            }
            solve();
            if (i + 1 < b) {
                in.readLine();
            }
        }
    }

    // calculate and print the three values for each grid
    private static void solve() {
        int score = 0;
        String best = "";
        int found = 0;

        for (String w: words) {
            if (find(w)) {
                int n = w.length();
                score += points[n];
                found++;
                if (n > best.length()) {
                    best = w;
                } else if (n == best.length()) {
                    best = w.compareTo(best) < 0 ? w : best;
                }
            }
        }

        System.out.printf("%d %s %d\n", score, best, found);
    }

    // look for matching start
    private static boolean find(String word) {
        visited = new boolean[4][4];
        boolean works = false;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (grid[i].charAt(j) == word.charAt(0)) {
                    works = works || recur(word, i, j);
                }
                if (works) {
                    return true;
                }
            }
        }
        return false;
    }

    // dfs in grid for word
    private static boolean recur(String word, int r, int c) {
        if (word.length() == 0) {
            return true;
        }

        if (r < 0 || r > 3 || c < 0 || c > 3 || visited[r][c] || word.charAt(0) != grid[r].charAt(c)) {
            return false;
        }

        visited[r][c] = true;
        boolean works = false;
        works = works || recur(word.substring(1), r+1, c);
        works = works || recur(word.substring(1), r-1, c);
        works = works || recur(word.substring(1), r, c+1);
        works = works || recur(word.substring(1), r, c-1);
        works = works || recur(word.substring(1), r-1, c-1);
        works = works || recur(word.substring(1), r-1, c+1);
        works = works || recur(word.substring(1), r+1, c-1);
        works = works || recur(word.substring(1), r+1, c+1);
        visited[r][c] = false;

        return works;
    }
}