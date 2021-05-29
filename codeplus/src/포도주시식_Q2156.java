import java.util.Scanner;

public class 포도주시식_Q2156 {
	public static void main(String[] args) {
		System.out.println(이차원_다이나믹스());
		System.out.println(일차원_다이나믹스());
	}

	static int 이차원_다이나믹스() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] d = new int[10001][3];
		int[] a = new int[10001];

		for (int i = 1; i <= n; i++) {
			a[i] = sc.nextInt();
		}

		for (int i = 1; i <= n; i++) {
			d[i][0] = Math.max(Math.max(d[i - 1][0], d[i - 1][1]), d[i - 1][2]) + 0;
			d[i][1] = d[i - 1][0] + a[i];
			d[i][2] = d[i - 1][1] + a[i];
		}

		return Math.max(Math.max(d[n][0], d[n][1]), d[n][2]);
	}

	static int 일차원_다이나믹스() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] d = new int[10001];
		int[] a = new int[10001];

		for (int i = 1; i <= n; i++) {
			a[i] = sc.nextInt();
		}

		d[1] = a[1];
		d[2] = a[1] + a[2];

		for (int i = 3; i <= n; i++) {
			d[i] = d[i - 1];
			if (d[i] < d[i - 2] + a[i]) {
				d[i] = d[i - 2] + a[i];
			}
			if (d[i] < d[i - 3] + a[i - 1] + a[i]) {
				d[i] = d[i - 3] + a[i - 1] + a[i];
			}
		}

		return d[n];
	}
}
