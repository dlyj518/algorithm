import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] rd = new int[n][2];
        int tmp = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (a > b) {tmp = b; b = a; a = tmp;}
            rd[i][0] = a; rd[i][1] = b;
        }
        int l = Integer.parseInt(br.readLine());
        Arrays.sort(rd, Comparator.comparingInt(x -> x[1]));
        int rs = 0;
        PriorityQueue<int[]> hq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });
        for (int[] r: rd) {
            if (r[1] - r[0] > l) continue;
            if (hq.isEmpty()) {hq.add(r); continue;}
            while (hq.peek()[0] < r[1] - l) {
                hq.poll();
                if (hq.isEmpty()) break;
            }
            hq.add(r);
            if (rs < hq.size()) rs = hq.size();
        }
        System.out.println(rs);
    }
}