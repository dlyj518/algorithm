import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int[] x = new int[3];
        for (int i = 0; i < 3; i++) x[i] = Integer.parseInt(s[i]);
        if (x[0] == x[1] && x[0] == x[2]) System.out.println(10000 + x[0] * 1000);
        else if (x[0] != x[1] && x[1] != x[2] && x[2] != x[0]) System.out.println(Math.max(Math.max(x[0], x[1]), x[2]) * 100);
        else if (x[0] == x[1] || x[0] == x[2]) System.out.println(1000 + x[0] * 100);
        else System.out.println(1000 + x[1] * 100);
    }
}