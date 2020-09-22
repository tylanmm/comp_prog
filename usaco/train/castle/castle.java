/*
ID: tylan071
LANG: JAVA
TASK: castle
*/

import java.io.*;
import java.util.*;

public class castle {
    static int[][] castle;
    static int M, N;

    public static void main(String[] args) throws IOException {
        // read input
        Scanner in = new Scanner(new File("castle.in"));
        M = in.nextInt();
        N = in.nextInt();
        castle = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                castle[i][j] = in.nextInt();
            }
        }
        in.close();

        // count number of rooms, find largest
        int numRooms = 0, maxRoom = 0;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (castle[r][c] < 16) {
                    numRooms += 1;
                    maxRoom = Math.max(maxRoom, floodfill(r, c));
                }
            }
        }
        reset();

        // find which wall to remove
        int maxModRoom = 0, R = 0, C = 0;
        char dir = 'N';
        for (int c = 0; c < M; c++) {
            for (int r = N-1; r >= 0; r--) {
                if (r > 0 && (castle[r][c] & 2) > 0) {
                    castle[r][c] -= 2;
                    int roomSize = floodfill(r, c);
                    castle[r][c] += 2;
                    reset();
                    if (roomSize > maxModRoom) {
                        maxModRoom = roomSize;
                        R = r; C = c; dir = 'N';
                    }
                }

                if (c < M-1 && (castle[r][c] & 4) > 0) {
                    castle[r][c] -= 4;
                    int roomSize = floodfill(r, c);
                    castle[r][c] += 4;
                    reset();
                    if (roomSize > maxModRoom) {
                        maxModRoom = roomSize;
                        R = r; C = c; dir = 'E';
                    }
                }
            }
        }

        // write out
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("castle.out")));
        out.println(numRooms);
        out.println(maxRoom);
        out.println(maxModRoom);
        out.println(String.format("%d %d %c", R+1, C+1, dir));
        out.close();
    }

    public static int floodfill(int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= M || castle[r][c] >= 16) {
            return 0;
        }

        int res = 1;
        castle[r][c] |= 16;

        // west
        if ((castle[r][c] & 1) == 0) {
            res += floodfill(r, c-1);
        }

        // north
        if ((castle[r][c] & 2) == 0) {
            res += floodfill(r-1, c);
        }
        
        // east
        if ((castle[r][c] & 4) == 0) {
            res += floodfill(r, c+1);
        }

        // south
        if ((castle[r][c] & 8) == 0) {
            res += floodfill(r+1, c);
        }

        return res;
    }

    public static void reset() {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (castle[r][c] >= 16) castle[r][c] -= 16;
            }
        }
    }
}