import java.util.Arrays;
import java.util.Scanner;

public class 단지번호붙이기_Q2667_DFS {

	private static int dx[] = {0, 0, 1, -1};
	private static int dy[] = {1, -1, 0, 0};
	private static int[] aparts = new int[25 * 25];
	private static int n;

	// 아파트 단지 번호의 수
	private static int apartNum = 0;
	private static boolean[][] visited = new boolean[25][25];
	private static int[][] map = new int[25][25];

	private static void dfs(int x, int y) {
		visited[x][y] = true;
		aparts[apartNum]++;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
				if (map[nx][ny] == 1 && !visited[nx][ny]) {
					dfs(nx, ny);
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		map = new int[n][n];
		visited = new boolean[n][n];

		// 전체 사각형 입력 받기
		for (int i = 0; i < n; i++) {
			String input = sc.next();
			for (int j = 0; j < n; j++) {
				map[i][j] = input.charAt(j) - '0';
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (map[i][j] == 1 && !visited[i][j]) {
					// 구역 별로 돌아갈 때마다 apartNum 추가!
					apartNum++;
					dfs(i, j);
				}
			}
		}

		Arrays.sort(aparts);
		System.out.println(apartNum);

		for (int i = 0; i < 25 * 25; i++) {
			if (aparts[i] != 0) {
				System.out.println(aparts[i]);
			}
		}
	}
}
