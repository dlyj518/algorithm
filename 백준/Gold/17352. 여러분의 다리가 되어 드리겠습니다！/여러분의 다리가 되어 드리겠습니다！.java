import java.io.*;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {
	static int[] pr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        pr = new int[n + 1];
        for (int i = 1; i < n + 1; i++) pr[i] = i;
        for (int i = 0; i < n - 2; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(st.nextToken()); int b = Integer.parseInt(st.nextToken());
        	a = fnd(a); b = fnd(b);
        	if (a > b) pr[a] = b; else pr[b] = a;        
		}
        Set<Integer> s = new TreeSet<Integer>();        
        for (int i = 1; i < n + 1; i++) s.add(fnd(pr[i]));
        for (Integer i : s) System.out.print(i + " ");
    }
    static int fnd(int i) {
    	if (i == pr[i]) return i;
    	return fnd(pr[i]);
    }
}