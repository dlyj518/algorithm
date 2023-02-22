import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(br.readLine());
        int a, b, c;
        if (m + x < 60) {a = h; b = m + x;}
        else {
            b = (m + x) % 60; c = (m + x) / 60;
            a =  c + h > 23 ? c + h - 24 : c + h;
        }
        System.out.println(a + " " + b);
    }
}