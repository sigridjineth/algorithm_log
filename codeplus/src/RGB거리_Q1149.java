import java.util.Scanner;

public class RGB거리_Q1149 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] a = new int[n + 1][3];
		int[][] d = new int[n + 1][3];

		for (int i = 1; i <= n; i++) {
			for (int j = 0; j < 3; j++) {
				a[i][j] = sc.nextInt();
			}
		}

		for (int i = 1; i <= n; i++) {
			d[i][0] = Math.min(d[i - 1][1], d[i - 1][2]) + a[i][0];
			d[i][1] = Math.min(d[i - 1][0], d[i - 1][2]) + a[i][1];
			d[i][2] = Math.min(d[i - 1][0], d[i - 1][1]) + a[i][2];
		}

		System.out.println(Math.min(Math.min(d[n][0], d[n][1]), d[n][2]));
	}
}
