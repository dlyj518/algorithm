import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String yn = br.readLine();
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> dice = new ArrayList();
        while (st.hasMoreTokens()){
            dice.add(Integer.parseInt(st.nextToken()));
        }
        dice.sort(Comparator.naturalOrder());
        HashSet<Integer> diceset = new HashSet<>(dice);
        int sumdice = 0;
        for (Integer d : dice) {
            sumdice += d;
        }
        int sum = 0;
        if (yn.charAt(10) == 'Y' && dice.get(0) == dice.get(2)) {
            sum = 50;
        } else if (diceset.size() > 2 && ((dice.get(0) != 1 && yn.charAt(9) == 'Y') || (dice.get(2) != 6 && yn.charAt(8) == 'Y'))) {
            sum = 30;
        } else if (yn.charAt(11) == 'Y') {
            sum += sumdice + 12;
        } else {
            if (diceset.size() < 3 && yn.charAt(7) == 'Y') {
                if (dice.get(0) == dice.get(2)) {
                    if (dice.get(0) == 6) {
                        sum = 28;
                    } else {
                        sum = Math.max(sum, sumdice + 12);
                    }
                } else if (dice.get(2) > dice.get(1)) {
                    sum = Math.max (sum, sumdice + dice.get(2) * 2);
                } else {
                    sum = Math.max(sum, sumdice + dice.get(2) + dice.get(0));
                }
            }
            if (diceset.size() < 3 && yn.charAt(6) == 'Y') {
                if (dice.get(0) == dice.get(1)) {
                    sum = Math.max(sum, 4 * dice.get(0));
                } else {
                    sum = Math.max(sum, 4 * dice.get(2));
                }
            }
            for (int i = 1; i < 7; i++) {
                if (yn.charAt(i - 1) == 'Y') {
                    sum = Math.max(sum, i * (Collections.frequency(dice, i) + 2));
                }
            }
        }
        System.out.println(sum);
    }
}