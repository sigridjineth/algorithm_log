import java.util.*;
import java.io.*;

public class 파일합치기_Q11066 {
    static int[] a;
    static int[][] d;
    public static int go(int i, int j) {
        if (i == j) {
            return 0;
        }
        if (d[i][j] != -1) {
            return d[i][j];
        }
        int ans = -1;
        int sum = 0;
        for (int k=i; k<=j; k++) {
            sum += a[k];
        }
        for (int k=i; k<=j-1; k++) {
            int temp = go(i, k) + go(k+1, j) + sum;
            if (ans == -1 || ans > temp) {
                ans = temp;
            }
        }
        d[i][j] = ans;
        return ans;
    }
  
    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(bf.readLine());
        while (t-- > 0) {
            int n = Integer.valueOf(bf.readLine());
            String[] nums = bf.readLine().split(" ");
            a = new int[n+1];
            d = new int[n+1][n+1];
            for (int i=1; i<=n; i++) {
                a[i] = Integer.valueOf(nums[i-1]);
                Arrays.fill(d[i], -1);
            }
            System.out.println(go(1, n));
        }
    }
}
