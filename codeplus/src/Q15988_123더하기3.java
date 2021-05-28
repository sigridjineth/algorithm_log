import java.util.Scanner;

public class Q15988_123더하기3 {
	static final long mod = 1_000_000_009;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		long[] dp = new long[1000001];
		dp[0] = 1;
		// 1, 2, 3까지는 자기 자신 가능하므로 직접 입력한다.
		dp[1] = 1;
		dp[2] = 2;
		dp[3] = 4;
		for (int i = 4; i <= 1_000_000; i++) {
			dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod;
		}

		while (t-- > 0) {
			int n = sc.nextInt();
			System.out.println(dp[n]);
		}
	}
}
