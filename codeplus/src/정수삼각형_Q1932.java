import java.util.Scanner;

public class 정수삼각형_Q1932 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] triangle = new int[n][n];
		int[][] dp = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				triangle[i][j] = sc.nextInt();
			}
		}
		dp[0][0] = triangle[0][0];
		for (int i = 1; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				dp[i][j] = dp[i - 1][j] + triangle[i][j];
				if (j - 1 >= 0 && dp[i][j] < dp[i - 1][j - 1] + triangle[i][j]) {
					dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
				}
			}
		}
		int ans = dp[n - 1][0];
		for (int i = 0; i < n; i++) {
			if (ans < dp[n - 1][i]) {
				ans = dp[n - 1][i];
			}
		}
		System.out.println(ans);
	}
}