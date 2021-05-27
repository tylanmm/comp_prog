import java.util.*;

public class cross {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char[][] grid = new char[9][9];
        HashMap<Character, HashSet<Integer>> rows = new HashMap<>();
        HashMap<Character, HashSet<Integer>> cols = new HashMap<>();
        for (char i = '1'; i <= '9'; i++) {
            rows.put(i, new HashSet<>());
            cols.put(i, new HashSet<>());
        }

        for (int i = 0; i < 9; i++) {
            String line = in.nextLine();
            for (int j = 0; j < 9; j++) {
                char c = line.charAt(j);
                grid[i][j] = c;
                if (c != '.') {
                    if (!(rows.get(c).add(i) && cols.get(c).add(j))) {
                        System.out.println("ERROR");
                        in.close();
                        return;
                    }
                }
            }
        }

        in.close();

        for (char i = '1'; i <= '9'; i++) {
            System.out.println(i);
            System.out.println(rows.get(i));
            System.out.println(cols.get(i) + "\n");
        }


    }
}