import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static ArrayList<ArrayList<Tuple>> rd;
    static final long INF = Long.MAX_VALUE;

    static long dijkstra() {
        PriorityQueue<Tuple> q = new PriorityQueue<>();
        q.offer(new Tuple(1, 1, 0L));
        long[][] vs = new long[N + 1][11];
        for (int i = 0; i < N + 1; i++)
            Arrays.fill(vs[i], INF);
        vs[1][1] = 0;
        while (!q.isEmpty()) {
            Tuple t = q.poll();
            int x = t.nn; int s = t.ss;
            long cost = t.ll;
            if (vs[x][s] < cost) continue;
            for (Tuple rr : rd.get(x)) {
                for (int d = -1; d <= 1; d++) {
                    int ss = s + d;
                    if (!(1 <= ss && ss <= rr.kk)) continue;
                    int yy = rr.nn;
                    long nt = cost + rr.ll / ss;
                    if (vs[yy][ss] > nt) {
                        vs[yy][ss] = nt;
                        q.offer(new Tuple(yy, ss, nt));
                    }
                }
            }
        }
        long mn = INF;
        for (int i = 1; i <= 10; i++)
            mn = Math.min(mn, vs[N][i]);
        return mn;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        rd = new ArrayList<>(N);
        for (int i = 0; i <= N; i++) rd.add(new ArrayList<>());
        int M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            rd.get(a).add(new Tuple(b, 2520L * l, k));
            rd.get(b).add(new Tuple(a, 2520L * l, k));
        }
        long x = dijkstra();
        System.out.print(x / 2520);
        x %= 2520;
        double y = (double)x / 2520;
        System.out.println(String.format("%.9f", y).toString().substring(1));
    }
}

class Tuple implements Comparable<Tuple> {
    int nn, ss, kk;
    long ll;
    Tuple(int n, long l, int k) {
        nn = n; ll = l; kk = k;
    }
    Tuple(int n, int s, long l) {
        nn = n; ss = s; ll = l;
    }
    @Override
    public int compareTo(Tuple o) { return Long.compare(ll, o.ll); }
}