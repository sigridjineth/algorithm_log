import java.util.Scanner;

public class 오르막수_Q11057 {
	static int[][] dp = new int[1001][10];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 0; i < 10; i++) {
			dp[1][i] = 1;
		}

		for (int i = 2; i <= n; i++) {
			for (int j = 0; j <= 10; j++) {
				for (int k = j; k < 10; k++) { // 마지막 수 판별은 k <= j이다.
					dp[i][j] = (dp[i][j] + dp[i - 1][k]) % 10007;
				}
			}
		}

		for (int i = 0; i < 10; i++) {
			answer = (answer + dp[n][i]) % 10007;
		}

		System.out.println(answer);
	}
}
