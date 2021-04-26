import java.util.Scanner;

public class NandMK_18290_3 {
	static int[][] a = new int[10][10];
	static boolean[][] c = new boolean[10][10];
	static int n, m, k;
	static int answer = -99999;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};

	static void go(int prev, int cnt, int sum) {
		if (cnt == k) {
			if (answer < sum) {
				answer = sum;
			}
			return;
		}

		for (int j = prev + 1; j < n * m; j++) {
			int x = j / m;
			int y = j % m;
			if (c[x][y]) {
				continue;
			}
			if (c[x][y]) {
				continue;
			}
			boolean ok = true;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < m) {
					if (c[nx][ny]) {
						ok = false;
					}
				}
			}
			if (ok) {
				c[x][y] = true;
				go(x * m + y, cnt + 1, sum + a[x][y]);
				c[x][y] = false;
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		k = sc.nextInt();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				a[i][j] = sc.nextInt();
			}
		}
		go(-1, 0, 0);
		System.out.println(answer);
	}
}
