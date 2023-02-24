import java.io.*;

public class Main {
    static int bsum(int a, int b) {
        if (a > 0) return 10 * a + b;
        return 10 * a - b;
    }
    public static void chk(int i, int z, int p, int r, String n) {
        if (i > z) {
            if (r == 0) System.out.println(n);
            return;
        }
        chk(i + 1, z, bsum(p, i), r - p + bsum(p, i), n +" " + i);
        chk(i + 1, z, i, r + i, n + '+' + i);
        chk(i + 1, z, -i, r - i, n + '-' + i);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            chk(2, n, 1, 1, "1");
            System.out.println();
        }
    }
}