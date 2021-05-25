import java.util.Scanner;

class 메모리_아끼기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[][] dp = new int[201][201];

		for (int i = 1; i <= k; i++) {
			dp[i][0] = 1;
		}

		for (int i = 1; i <= k; i++) {
			for (int j = 1; j <= n; j++) {
				dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000;
			}
		}

		System.out.println(dp[k][n]);
	}
}

public class 합분해_Q2225 {
	private static final long[][] d = new long[201][201];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();

		d[0][0] = 1;

		for (int i = 1; i <= k; i++) {
			for (int j = 0; j <= n; j++) {
				for (int l = 0; l <= j; l++) {
					d[i][j] += d[i - 1][j - l];
					d[i][j] %= 1000000000;
				}
			}
		}

		System.out.println(d[k][n]);
	}
}
