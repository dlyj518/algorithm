import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] dx = {0, 0, -1, 1}; int[] dy = {1, -1, 0, 0};
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[][] mp = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) mp[i][j] = Integer.parseInt(st.nextToken());
        }
        int[] cm = new int[k];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) cm[i] = Integer.parseInt(st.nextToken()) - 1;
        int[] dc = new int[6];
        int[][] sp = new int[4][6];
        sp[0] = new int[] {0, 4, 2, 5, 3, 1};
        sp[1] = new int[] {0, 5, 2, 4, 1, 3};
        sp[2] = new int[] {1, 2, 3, 0, 4, 5};
        sp[3] = new int[] {3, 0, 1, 2, 4, 5};
        for (int d: cm) {
            int nx = x + dx[d]; int ny = y + dy[d];
            if (0 > nx || nx >= n || 0 > ny || ny >= m) continue;
            int[] nd = new int[6];
            for (int i = 0; i < 6; i++) nd[i] = dc[sp[d][i]];
            if (mp[nx][ny] > 0) {
                nd[3] = mp[nx][ny]; mp[nx][ny] = 0;
            } else mp[nx][ny] = nd[3];
            System.out.println(nd[1]);
            x = nx; y = ny; dc = nd;
        }
    }
}