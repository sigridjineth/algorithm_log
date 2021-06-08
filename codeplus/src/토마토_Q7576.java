import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Pair_Tomato {
	int x;
	int y;
	Pair_Tomato(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class 토마토_Q7576 {
	public static final int[] dx = {0, 0, 1, -1};
	public static final int[] dy = {1, -1, 0, 0};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = sc.nextInt();
		int[][] a = new int[n][m];
		int[][] time = new int[n][m];
		Queue<Pair_Tomato> queue = new LinkedList<>();

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				a[i][j] = sc.nextInt();
				time[i][j] = -1; // default value
				if (a[i][j] == 1) {
					queue.add(new Pair_Tomato(i, j));
					time[i][j] = 0; // on the queue! first frontier!
				}
			}
		}

		while (!queue.isEmpty()) {
			Pair_Tomato pair = queue.remove();
			int x = pair.x;
			int y = pair.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
					if (a[nx][ny] == 0 && time[nx][ny] == -1) {
						queue.add(new Pair_Tomato(nx, ny));
						time[nx][ny] = time[x][y] + 1;
					}
				}
			}
		}

		int ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (ans < time[i][j]) {
					ans = time[i][j];
				}
			}
		}


		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] == 0 && time[i][j] == -1) {
					ans = -1;
					break;
				}
			}
		}

		System.out.println(ans);
	}
}
