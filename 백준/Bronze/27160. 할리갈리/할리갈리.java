import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<String, Integer> card = new HashMap<>();
        card.put("STRAWBERRY", 0);
        card.put("BANANA", 0);
        card.put("LIME", 0);
        card.put("PLUM", 0);
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String f = st.nextToken();
            card.put(f, card.get(f) + Integer.parseInt(st.nextToken()));
        }
        boolean check = false;
        for (String x : card.keySet()) {
            if (card.get(x) == 5) {
                check = true;
                System.out.println("YES");
                break;
            }
        }
        if (!check) {
            System.out.println("NO");
        }

    }
}
