import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class AlgospotPair {
	int y;
	int x;

	AlgospotPair(int y, int x) {
		this.y = y;
		this.x = x;
	}
}


public class 알고스팟_Q1261 {
	public static int[] dx = {0, 0, 1, -1};
	public static int[] dy = {1, -1, 0, 0};

	public static void 더블큐를_사용한다() {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = sc.nextInt();
		sc.nextLine();
		int[][] a = new int[n][m];
		int[][] d = new int[n][m];
		for (int i = 0; i < n; i++) {
			String s = sc.nextLine();
			Arrays.fill(d[i], Integer.MAX_VALUE);
			for (int j = 0; j < m; j++) {
				a[i][j] = s.charAt(j) - '0';
			}
		}
		Queue<AlgospotPair> current_least_queue = new LinkedList<>();
		Queue<AlgospotPair> next_least_queue = new LinkedList<>();
		current_least_queue.offer(new AlgospotPair(0, 0));
		d[0][0] = 0;
		while (!current_least_queue.isEmpty()) {
			AlgospotPair pair = current_least_queue.poll();
			int x = pair.x;
			int y = pair.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (0 <= nx && nx < m && 0 <= ny && ny < n) {
					// a[ny][nx]가 벽이면서 방문하지 않았거나, 방문 기록이 있지만 현재 액션을 통하면 해당 좌표의 벽을 깨는 횟수를 더 줄일 수 있다고 할 때
					// d[ny][nx] = d[y][x] + 1로 최적화를 해 주면 해당 좌표의 벽을 깨는 횟수의 최솟값이 갱신됩니다.
					if (a[ny][nx] == 1 && (d[ny][nx] == Integer.MAX_VALUE || d[ny][nx] > d[y][x] + 1)) {
						d[ny][nx] = d[y][x] + 1;
						next_least_queue.add(new AlgospotPair(ny, nx));
						// a[ny][nx]가 벽이 아니면서 방문하지 않았거나, 방문 기록이 있지만 현재 액션을 통하면 해당 좌표의 벽을 깨는 횟수를 더 줄일 수 있다고 할 때
						// d[ny][nx] = d[y][x]로 최적화를 해 주면 해당 좌표의 벽을 깨는 횟수의 최솟값이 갱신됩니다.
					} else if (a[ny][nx] == 0 && (d[ny][nx] == Integer.MAX_VALUE || d[ny][nx] > d[y][x])) {
						d[ny][nx] = d[y][x];
						current_least_queue.add(new AlgospotPair(ny, nx));
					}
				}
			}
			if (current_least_queue.isEmpty()) {
				current_least_queue = next_least_queue;
				next_least_queue = new LinkedList<>();
			}
		}
		System.out.println(d[n - 1][m - 1]);
	}

	public static void Deque를_사용한다() {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = sc.nextInt();
		sc.nextLine();
		int[][] a = new int[n][m];
		int[][] d = new int[n][m];
		for (int i = 0; i < n; i++) {
			String s = sc.nextLine();
			Arrays.fill(d[i], Integer.MAX_VALUE);
			for (int j = 0; j < m; j++) {
				a[i][j] = s.charAt(j) - '0';
			}
		}
		ArrayDeque<AlgospotPair> deque = new ArrayDeque<>();
		deque.add(new AlgospotPair(0, 0));
		d[0][0] = 0;
		while (!deque.isEmpty()) {
			AlgospotPair pair = deque.poll();
			int x = pair.x;
			int y = pair.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (0 <= nx && nx < m && 0 <= ny && ny < n) {
					// a[ny][nx]가 벽이면서 방문하지 않았거나, 방문 기록이 있지만 현재 액션을 통하면 해당 좌표의 벽을 깨는 횟수를 더 줄일 수 있다고 할 때
					// d[ny][nx] = d[y][x] + 1로 최적화를 해 주면 해당 좌표의 벽을 깨는 횟수의 최솟값이 갱신됩니다.
					if (a[ny][nx] == 1 && (d[ny][nx] == Integer.MAX_VALUE || d[ny][nx] > d[y][x] + 1)) {
						d[ny][nx] = d[y][x] + 1;
						deque.addFirst(new AlgospotPair(ny, nx));
						// a[ny][nx]가 벽이 아니면서 방문하지 않았거나, 방문 기록이 있지만 현재 액션을 통하면 해당 좌표의 벽을 깨는 횟수를 더 줄일 수 있다고 할 때
						// d[ny][nx] = d[y][x]로 최적화를 해 주면 해당 좌표의 벽을 깨는 횟수의 최솟값이 갱신됩니다.
					} else if (a[ny][nx] == 0 && (d[ny][nx] == Integer.MAX_VALUE || d[ny][nx] > d[y][x])) {
						d[ny][nx] = d[y][x];
						deque.addLast(new AlgospotPair(ny, nx));
					}
				}
			}
		}
		System.out.println(d[n - 1][m - 1]);
	}

	public static void main(String[] args) {
		더블큐를_사용한다();
		Deque를_사용한다();
	}
}
