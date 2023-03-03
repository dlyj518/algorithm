import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t -- > 0) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int n = Integer.parseInt(st.nextToken());
        	if (n < 4) {System.out.println("YES"); continue;}
        	int[] x = new int[n + 1];
        	for (int i = 1; i <= n; i++) x[i] = Integer.parseInt(st.nextToken());
        	long a = -x[1] + 3 * x[2] - 3 * x[3] + x[4]; 
        	long b = 9 * x[1] - 24 * x[2] + 21 * x[3] - 6 * x[4]; 
        	long c = -26 * x[1] + 57 * x[2] - 42 * x[3] + 11 * x[4]; 
        	long d = 24 * x[1] - 36 * x[2] + 24 * x[3] - 6 * x[4]; 
        	int y = 1;
        	for (long i = 5; i <= n; i++) {
				if (a * i * i * i + b * i * i + c * i + d != x[(int) i] * 6) {y = 0; break;}
			}
        	System.out.println(y == 1 ? "YES" : "NO");
		}
    }
}