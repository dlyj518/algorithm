import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int a = Integer.parseInt(line[1]);
        int l = Integer.parseInt(line[2]);
        int[][] dp = new int[n + 1][l + 1];
        int[][] lg = new int[n + 1][l + 1];
        int[][] ln = new int[n][2];
        for (int i = 0; i < n; i++) {
            line = br.readLine().split(" ");
            Arrays.fill(dp[i], -1);
            Arrays.fill(lg[i], -1);
            for (int j = 0; j < 2; j++) ln[i][j] = Integer.parseInt(line[j]);
        }
        Arrays.fill(dp[n], -1);
        Arrays.fill(lg[n], -1);
        dp[0][l] = a;
        for (int i = 0; i < n; i++) {
            int x = ln[i][0];
            int y = ln[i][1];
            for (int j = 1; j <= l; j++) {
                if (dp[i][j] == -1) continue;
                if (y >= 0 && j > y && dp[i + 1][j - y] < dp[i][j]) {
                    dp[i + 1][j - y] = dp[i][j];
                    lg[i + 1][j - y] = y;
                }
                if (x >= 0) {
                    int mx = dp[i][j] - x;
                    if (y < 0 && mx < 0) mx = 0;
                    if (dp[i + 1][j] < mx) {
                        dp[i + 1][j] = mx;
                        lg[i + 1][j] = 0;
                    }
                }
            }
        }
        List<Character> rst = new ArrayList<>();
        int q = 1;
        for (int i = 1; i <= l; i++) {
            if (lg[n][i] != -1) {
                System.out.println("YES");
                int k = i;
                for (int j = n; j > 0; j--) {
                    if (lg[j][k] != 0 || ln[j - 1][1] == 0) rst.add('L');
                    else rst.add('A');
                    k += lg[j][k];
                }
                for (int j = rst.size() - 1; j >= 0; j--) System.out.print(rst.get(j));
                q = 0;
                break;
            }
        } 
        if (q == 1) System.out.println("NO");
    }
}