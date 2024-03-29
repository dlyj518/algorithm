import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int b = Integer.parseInt(st.nextToken()); int c = Integer.parseInt(st.nextToken());
        long r = 0;
        for (int ai: a) {
            r += 1;
            if ((ai - b) > 0) {r += (ai - b) / c; r += (ai - b) % c > 0 ? 1 : 0;}
        }
        System.out.println(r);
    }
}