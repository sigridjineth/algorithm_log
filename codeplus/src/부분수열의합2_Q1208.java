import java.util.*;

public class 부분수열의합2_Q1208 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] a = new int[n];
        for (int i=0; i<n; i++) {
            a[i] = sc.nextInt();
        }
        int m = n/2;
        n = n-m;
        int[] first = new int[1<<n];
        for (int i=0; i<(1<<n); i++) {
            for (int k=0; k<n; k++) {
                if ((i&(1<<k)) == (1<<k)) {
                    first[i] += a[k];
                }
            }
        }
        int[] second = new int[1<<m];
        for (int i=0; i<(1<<m); i++) {
            for (int k=0; k<m; k++) {
                if ((i&(1<<k)) == (1<<k)) {
                    second[i] += a[k+n];
                }
            }
        }
        Arrays.sort(first);
        Arrays.sort(second);
        n = (1<<n);
        m = (1<<m);
        for (int i=0; i<m/2; i++) {
            int temp = second[i];
            second[i] = second[m-i-1];
            second[m-i-1] = temp;
        }
        int i = 0;
        int j = 0;
        long ans = 0;
        while (i < n && j < m) {
            if (first[i] + second[j] == s) {
                long c1 = 1;
                long c2 = 1;
                while (i < n && first[i] == first[i+1]) {
                    c1 += 1;
                    i += 1;
                }
                while (j < m && second[j] == second[j+1]) {
                    c2 += 1;
                    j += 1;
                }
                ans += c1*c2;
            } else if (first[i] + second[j] < s) {
                i += 1;
            } else {
                j += 1;
            }
        }
        if (s == 0) ans -= 1;
        System.out.println(ans);
    }
}
