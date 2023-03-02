import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); int l = Integer.parseInt(st.nextToken());
        int[][] mp = new int[n][n];
        int r = 0;
        for (int i = 0; i < n; i++) {
        	st = new StringTokenizer(br.readLine());
        	int c = 1; int p = 1;
			for (int j = 0; j < n; j++) {
				mp[i][j] = Integer.parseInt(st.nextToken());
				if (j != 0 && p > 0) {
					if (mp[i][j] == mp[i][j - 1]) {c += 1; 
					} else if (mp[i][j] - 1 == mp[i][j - 1]) {
						if (c < l) {p = 0; continue;}
						c = 1;
					} else if (mp[i][j] + 1 == mp[i][j - 1]) {
						if (c < 0) {p = 0; continue;}
						c = - l + 1;
					} else p = 0;
				}
			}
			if (p > 0 && c >= 0) r += 1;
		}
        for (int i = 0; i < n; i++) {
        	int c = 1; int p = 1;
			for (int j = 0; j < n; j++) {
				if (j != 0 && p > 0) {
					if (mp[j][i] == mp[j - 1][i]) {c += 1; 
					} else if (mp[j][i] - 1 == mp[j - 1][i]) {
						if (c < l) {p = 0; continue;}
						c = 1;
					} else if (mp[j][i] + 1 == mp[j - 1][i]) {
						if (c < 0) {p = 0; continue;}
						c = - l + 1;
					} else p = 0;
				}
			}
			if (p > 0 && c >= 0) r += 1;
		}
        System.out.println(r);
    }
}