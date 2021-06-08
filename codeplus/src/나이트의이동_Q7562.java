import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Pair_Night {
	int x;
	int y;
	Pair_Night(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class 나이트의이동_Q7562 {
	static final int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2};
	static final int[] dy = {1, 2, 2, 1, -1, -2, -2, -1};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while (t-- > 0) {
			int n = sc.nextInt();
			int starting_x = sc.nextInt();
			int starting_y = sc.nextInt();
			int ending_x = sc.nextInt();
			int ending_y = sc.nextInt();

			int[][] d = new int[n][n];
			for (int i = 0; i < n; i++) {
				Arrays.fill(d[i], -1);
			}

			Queue<Pair_Night> queue = new LinkedList<>();
			queue.add(new Pair_Night(starting_x, starting_y));
			d[starting_x][starting_y] = 0;
			while (!queue.isEmpty()) {
				Pair_Night pair = queue.remove();
				int x = pair.x;
				int y = pair.y;
				for (int k = 0; k < 8; k++) {
					int nx = x + dx[k];
					int ny = y + dy[k];
					if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
						if (d[nx][ny] == -1) {
							d[nx][ny] = d[x][y] + 1;
							queue.add(new Pair_Night(nx, ny));
						}
					}
				}
			}
			System.out.println(d[ending_x][ending_y]);
		}
	}
}
