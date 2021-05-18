import java.util.Scanner;

// Top-Down
class TopDown {
	static final long mod = 1000000009L;
	static final int limit = 100000;
	static long[][] d = new long[limit + 1][4];

	static long go(int i, int num) {
		if (i < 0) return 0;
		if (num == i) return 1;
		if (d[i][num] != 0) return d[i][num];

		if (num == 1) {
			d[i][num] = go(i - 1, 2) + go(i - 1, 3);
			d[i][num] %= mod;
		}

		if (num == 2) {
			d[i][num] = go(i - 2, 1) + go(i - num, 3);
			d[i][num] %= mod;
		}

		if (num == 3) {
			d[i][num] = go(i - num, 1) + go(i - num, 2);
			d[i][num] %= mod;
		}

		return d[i][num];
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();

		while (t-- > 0) {
			int i = sc.nextInt();
			System.out.println((go(i, 1) + go(i, 2) + go(i, 3)) % mod);
		}
	}
}

// Bottom-Up
public class Q15990_123더하기5 {
	static final long mod = 1000000009L;
	static final int limit = 100000;
	static long[][] d = new long[limit + 1][4];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int i = 1; i <= limit; i++) {
			if (i - 1 >= 0) {
				d[i][1] = d[i - 1][2] + d[i - 1][3];
				if (i == 1) {
					d[i][1] = 1;
				}
			}
			if (i - 2 >= 0) {
				d[i][2] = d[i - 2][1] + d[i - 2][3];
				if (i == 2) {
					d[i][2] = 1;
				}
			}
			if (i - 3 >= 0) {
				d[i][3] = d[i - 3][1] + d[i - 3][2];
				if (i == 3) {
					d[i][3] = 1;
				}
			}
			d[i][1] %= mod;
			d[i][2] %= mod;
			d[i][3] %= mod;
		}
		int t = sc.nextInt();
		while (t-- > 0) {
			int n = sc.nextInt();
			System.out.println((d[n][1] + d[n][2] + d[n][3]) % mod);
		}
	}
}
