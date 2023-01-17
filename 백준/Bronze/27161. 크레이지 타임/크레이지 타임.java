import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int x = 1;
        int h = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            String c = st.nextToken();
            int k = Integer.parseInt(st.nextToken());
            h = h + x;
            if (h > 12) { h -= 12;
            } else if (h < 1) { h += 12;
            }
            boolean ch = h == k;
            boolean rh = Objects.equals(c, "HOURGLASS");
            String sy = "NO";
            if (ch != rh) {
                if (ch) { sy = "YES";
                } else { x *= -1; }
            }
            System.out.println(h + " " + sy);
        }
    }
}