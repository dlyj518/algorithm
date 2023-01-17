import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int sum = 0;
        int before = 0;
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            if (x != before + 1) {
                sum += x;
            }
            before = x;
        }
        System.out.println(sum);
    }
}
