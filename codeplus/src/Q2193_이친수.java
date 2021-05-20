import java.util.Scanner;

public class Q2193_이친수 {
	// 일차원 다이나믹스 Top-down
	public static long[] d = new long[91];
	public static long getPinaryNumber(int n) {
		if (n <= 2) {
			return 1;
		} else if (d[n] > 0) {
			return d[n];
		} else {
			d[n] = getPinaryNumber(n - 1) + getPinaryNumber(n - 2);
			return d[n];
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		d[1] = 1;
		d[2] = 2;
		System.out.println(getPinaryNumber(n));
	}
}


// 일차원 다이나믹스 Bottom-up
class 일차원_다이나믹스_바텀업 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] d = new long[n + 1];

		if (n <= 2) {
			System.out.println(1);
			return;
		}

		d[1] = 1;
		d[2] = 1;

		for (int i = 3; i <= n; i++) {
			d[i] = d[i - 1] + d[i - 2];
		}

		System.out.println(d[n]);
	}
}

class 이차원_바텀업 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[][] d = new long[n + 1][2];

		if (n <= 2) {
			System.out.println(1);
			return;
		}

		d[1][0] = d[1][1] = d[2][0] = 1;
		d[2][1] = 0;

		for (int i = 3; i <= n; i++) {
			d[i][0] = d[i - 1][0] + d[i - 1][1];
			d[i][1] = d[i - 1][0];
		}

		System.out.println(d[n][0] + d[n][1]);
	}
}
