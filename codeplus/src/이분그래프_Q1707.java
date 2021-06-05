import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 이분그래프_Q1707 {
	static ArrayList<Integer>[] a;
	static int[] color;

	public static boolean dfs(int x, int c) {
		color[x] = c;
		for (int y : a[x]) {
			if (color[y] == 0) {
				if (!dfs(y, 3 - c)) {
					return false;
				}
			} else if (color[y] == color[x]) {
				return false;
			}
		}
		return true;
	}

	public static void dfs식_풀이() {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while (t-- > 0) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			a = new ArrayList[n + 1];
			for (int i = 1; i <= n; i++) {
				a[i] = new ArrayList<>();
			}
			for (int i = 0; i < m; i++) {
				int u = sc.nextInt();
				int v = sc.nextInt();
				a[u].add(v);
				a[v].add(u);
			}
			color = new int[n + 1];
			for (int i = 1; i <= n; i++) {
				if (color[i] == 0) {
					boolean result = dfs(1, i);
					if (!result) {
						System.out.println("NO");
						System.exit(0);
					}
				}
			}
			System.out.println("YES");
		}
	}

	public static boolean bfs(int start) {
		// 전달된 번호부터 탐색 수행
		color[start] = 1;
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(start);
		while (!queue.isEmpty()) {
			// 현재 위치에서 시작
			int c = queue.poll();
			for (int i: a[c]) {
				// 아직 방문하지 않은 정점이라면 큐에 넣고 현재 색상과 다른 색상으로 저장
				if (color[i] == 0) {
					queue.offer(i);
					color[i] = (3 - color[c]);
					// 이미 방문한 전력이 있다면
				} else {
					if (color[i] == color[c]) {
						return false;
					}
				}
			}
		}
		return true;
	}

	public static void bfs식_풀이() {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-- > 0) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			a = new ArrayList[n + 1];
			color = new int[n + 1];
			for (int i = 1; i <= n; i++) {
				a[i] = new ArrayList<>();
			}
			for (int i = 0; i < m; i++) {
				int u = sc.nextInt();
				int v = sc.nextInt();
				a[u].add(v);
				a[v].add(u);
			}
			// bfs 탐색을 통해 이분 그래프인지 확인
			for (int i = 1; i <= n; i++) {
				if (color[i] == 0) {
					boolean result = bfs(i);
					if (!result) {
						System.out.println("NO");
						System.exit(0);
					}
				}
			}
			System.out.println("YES");
		}
	}

	public static void main(String[] args) {
		dfs식_풀이();
		bfs식_풀이();
	}
}
