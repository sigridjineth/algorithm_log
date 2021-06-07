import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 단지번호붙이기_Q2667_BFS {

	private static int dx[] = {0, 0, 1, -1};
	private static int dy[] = {1, -1, 0, 0};
	private static int[] aparts = new int[25 * 25];
	private static int n;
	private static int apartNum = 0; // 아파트 단지 번호의 수
	private static boolean[][] visited = new boolean[25][25];
	private static int[][] map = new int[25][25];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		map = new int[n][n];
		visited = new boolean[n][n];

		// 전체 사각형 입력 받기
		for (int i = 0; i < n; i++) {
			String input = sc.next();
			for (int j = 0; j < n; j++) {
				map[i][j] = input.charAt(j) - '0'; // 아스키 코드 - 48
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (map[i][j] == 1 && !visited[i][j]) {
					apartNum++;
					bfs(i, j);
				}
			}
		}

		// 오름차순으로 정렬
		Arrays.sort(aparts);
		System.out.println(apartNum);

		// 아파트가 세 개라면 aparts에는 세 개만 update 된다.
		for (int apart : aparts) {
			if (apart != 0) {
				System.out.println(apart);
			}
		}
	}

	private static void bfs(int x, int y) {
		Queue<int[] > queue = new LinkedList<>();
		queue.add(new int[]{x, y});
		visited[x][y] = true;
		aparts[apartNum]++;

		while (!queue.isEmpty()) {
			// x, y 값을 받아보기 위한 방법
			int curX = queue.peek()[0];
			int curY = queue.peek()[1];
			queue.poll();

			for (int i = 0; i < 4; i++) {
				int nx = curX + dx[i];
				int ny = curY + dy[i];
				if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
					if (map[nx][ny] == 1 && !visited[nx][ny]) {
						queue.add(new int[]{nx, ny});
						visited[nx][ny] = true;
						aparts[apartNum]++;
					}
				}
			}
		}
	}
}
