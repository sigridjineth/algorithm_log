import java.util.*;
public class Main {
    static boolean next_permutation(int[] a) {
        int i = a.length-1;
        while (i > 0 && a[i-1] >= a[i]) {
            i -= 1;
        }

        if (i <= 0) {
            return false;
        }

        int j = a.length-1;
        while (a[j] <= a[i-1]) {
            j -= 1;
        }

        int temp = a[i-1];
        a[i-1] = a[j];
        a[j] = temp;

        j = a.length-1;
        while (i < j) {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            i += 1;
            j -= 1;
        }
        return true;
    }
    static int[] alpha = new int[256];
    static int calc(String[] a, Character[] letters, int[] d) {
        int m = letters.length;
        int sum = 0;
        for (int i=0; i<m; i++) {
            alpha[letters[i]] = d[i];
        }
        for (String s : a) {
            int now = 0;
            for (char x : s.toCharArray()) {
                now = now * 10 + alpha[x];
            }
            sum += now;
        }
        return sum;
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] a = new String[n];
        HashSet<Character> s = new HashSet<>();
        for (int i=0; i<n; i++) {
            a[i] = sc.next();
            for (char x : a[i].toCharArray()) {
                s.add(x);
            }
        }
        Character[] letters = s.toArray(new Character[s.size()]);
        int m = letters.length;
        int[] d = new int[m];
        for (int i=0; i<m; i++) {
            d[i] = 9-i;
        }
        Arrays.sort(d);
        int ans = 0;
        do {
            int now = calc(a, letters, d);
            if (ans < now) {
                ans = now;
            }
        } while(next_permutation(d));
        System.out.println(ans);
    }
}
