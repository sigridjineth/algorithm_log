import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Pair {
	int x;
	int y;
	Pair(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class 미로탐색_Q2178 {

	public static final int[] dx = {0, 0, 1, -1};
	public static final int[] dy = {1, -1, 0, 0};
	public static int[][] a;
	public static int[][] dist;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		a = new int[n][m];
		for (int i = 0; i < n; i++) {
			String s = sc.nextLine();
			for (int j = 0; j < m; j++) {
				a[i][j] = s.charAt(j) - '0';
			}
		}
		dist = new int[n][m];
		boolean[][] check = new boolean[n][m];
		Queue<Pair> q = new LinkedList<>();
		q.add(new Pair(0, 0));
		check[0][0] = true;
		dist[0][0] = 1;

		while (!q.isEmpty()) {
			Pair p = q.remove();
			int x = p.x;
			int y = p.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
					if (!check[nx][ny] && a[nx][ny] == 1) {
						q.add(new Pair(nx, ny));
						dist[nx][ny] = dist[x][y] + 1;
						check[nx][ny] = true;
					}
				}
			}
		}
		System.out.println(dist[n - 1][m - 1]);
	}
}
