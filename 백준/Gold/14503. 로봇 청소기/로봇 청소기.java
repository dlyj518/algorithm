import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int y = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int[] dy = new int[] {-1, 0, 1, 0}; int[] dx = new int[] {0, 1, 0, -1};
        int[][] mp = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) mp[i][j] = Integer.parseInt(st.nextToken());
        }
        int r = 0;
        while (true) {
            if (mp[y][x] == 0) {r += 1; mp[y][x] = -1;}
            int c = 0;
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i]; int nx = x + dx[i];
                if (mp[ny][nx] == 0) c += 1;
            }
            if (c == 0) {
                int nd = (d + 2) % 4;
                if (mp[y + dy[nd]][x + dx[nd]] == 1) break;
                y += dy[nd]; x += dx[nd];
            } else {
                d = (d + 3) % 4;
                int mx = mp[y + dy[d]][x + dx[d]];
                if (mx == 0) {y += dy[d]; x += dx[d];}
            }
        }
        System.out.println(r);
    }
}