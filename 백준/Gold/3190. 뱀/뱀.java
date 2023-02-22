import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};
        int d = 1;
        int[][] mp = new int[n][n];
        mp[0][0] = 1;
        int [] ap;
        Queue<String[]> cm = new LinkedList<>();
        Queue<int[]> sn = new LinkedList<>();
        sn.add(new int[] {0, 0});
        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            mp[y - 1][x - 1] = 9;
        }
        int l = Integer.parseInt(br.readLine());
        for (int i = 0; i < l; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            String b = st.nextToken();
            cm.add(new String[] {a, b});
        }
        int t = 0; int q = 1; int y = 0; int x = 0;
        String[] arr = cm.poll();
        int z = Integer.parseInt(arr[0]);
        String c = arr[1];
        while (q > 0) {
            t ++; y += dy[d]; x += dx[d];
            if (0 <= y && y < n && 0 <= x && x < n) {
                sn.add(new int[] {y, x});
                if (mp[y][x] != 1) {
                    if (mp[y][x] != 9) {
                        int[] ab = sn.poll();
                        mp[ab[0]][ab[1]] = 0;
                    }
                    mp[y][x] = 1;
                } else {q = 0; break;}
            } else break;
            if (t == z) {
                d += ("D".equals(c)) ? 1 : -1;
                d = (d > 3) ? 0 : (d < 0) ? 3: d;
                if (!cm.isEmpty()) {
                    arr = cm.poll();
                    z = Integer.parseInt(arr[0]);
                    c = arr[1];
                }
            }
        }
        System.out.println(t);
    }
}