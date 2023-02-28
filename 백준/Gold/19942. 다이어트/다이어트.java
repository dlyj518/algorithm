import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int mn = Integer.MAX_VALUE;
    static int[] m = new int[4];
    static ArrayList<Integer> l;
    static int[][] fd;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) m[i] = Integer.parseInt(st.nextToken());
        fd = new int[n][5];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++)  fd[i][j] = Integer.parseInt(st.nextToken());
        }
        dfs(0, 0, 0, 0, 0, 0, new ArrayList<>());
        if (mn == Integer.MAX_VALUE) System.out.println(-1);
        else {
            System.out.println(mn);
            for (int i : l) System.out.print(i + " ");
		}
    }
    static void dfs(int i, int p, int f, int s, int v, int c, ArrayList ll) {
        if (c > mn) return;
        if (m[0] <= p && m[1] <= f && m[2] <= s && m[3] <= v && c < mn) {l = ll; mn = c;}
        if (i >= n) return;
        dfs(i + 1, p + fd[i][0], f + fd[i][1], s + fd[i][2], v + fd[i][3], c + fd[i][4], new ArrayList<>(ll) {{add(i + 1);}});
        dfs(i + 1, p, f, s, v, c, ll);
        return;
    }
}