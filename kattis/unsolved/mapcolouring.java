import java.io.*;
import java.util.*;

public class mapcolouring {
    public static Scanner in = new Scanner(System.in);
    public static ArrayList<ArrayList<Integer>> components;
    public static ArrayList<ArrayList<Integer>> graph;
    public static int[] colors;
    public static int lo;

    public static void main(String[] args) {
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            int c = in.nextInt();
            int b = in.nextInt();
            buildGraph(c, b);
            findComponents();
            colors = new int[c];
            solve();
        }
    }

    public static void buildGraph(int c, int b) {
        graph = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < c; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < b; i++) {
            int j = in.nextInt();
            int k = in.nextInt();
            graph.get(j).add(k);
            graph.get(k).add(j);
        }
    }

    public static void findComponents() {
        boolean[] visited = new boolean[graph.size()];
        components = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < graph.size(); i++) {
            if (!visited[i]) {
                ArrayList<Integer> component = new ArrayList<Integer>();
                dfs(i, component, visited);
                components.add(component);
            }
        }
    }

    public static void dfs(int country, ArrayList<Integer> component, boolean[] visited) {
        visited[country] = true;
        component.add(country);
        for (int neighbor : graph.get(country)) {
            if (!visited[neighbor]) {
                dfs(neighbor, component, visited);
            }
        }
    }

    public static void solve() {
        lo = 5;
        for (ArrayList<Integer> component : components) {
            color(component.get(0), component);
        }
        System.out.println(lo < 5 ? lo : "many");
    }

    public static void color(int country, ArrayList<Integer> component) {
        HashSet<Integer> possibleColors = new HashSet<Integer>();
        for (int i = 1; i < 5; i++) possibleColors.add(i);

        for (int neighbor : graph.get(country)) {
            if (possibleColors.contains(colors[neighbor])) {
                possibleColors.remove(colors[neighbor]);
            }
        }

        if (possibleColors.size() == 0) {
            return;
        }
        
        int minPoss = 5;
        for (int color : possibleColors) { minPoss = Math.min(minPoss, color); }
        int numColored = 0;
        int maxColor = 0;
        for (int n : component) {
            numColored += (colors[n] == 0) ? 0 : 1;
            maxColor = Math.max(maxColor, colors[n]);
        }
        if (numColored + 1 == component.size()) {
            lo = Math.min(lo, Math.max(maxColor, minPoss));
            return;
        }

        for (int color : possibleColors) {
            colors[country] = color;
            for (int neighbor : graph.get(country)) {
                if (colors[neighbor] == 0) {
                    color(neighbor, component);
                }
            }
            colors[country] = 0;
        }
    }
}