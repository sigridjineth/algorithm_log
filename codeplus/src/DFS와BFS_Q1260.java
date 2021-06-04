import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class DFS와BFS_Q1260 {
	static ArrayList<Integer>[] a;
	static int[][] map;
	static boolean[] c;
	public static void dfs(int x) {
		if (c[x]) {
			return;
		}
		c[x] = true;
		System.out.print(x + " ");
		for (int y: a[x]) {
			if (!c[y]) {
				dfs(y);
			}
		}
	}
	public static void bfs(int start) {
		Queue<Integer> q = new LinkedList<>();
		q.add(start);
		c[start] = true;
		while (!q.isEmpty()) {
			int x = q.remove();
			System.out.print(x + " ");
			for (int y: a[x]) {
				if (!c[y]) {
					c[y] = true;
					q.add(y);
				}
			}
		}
	}

	public static void 인접리스트_이용() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int start = sc.nextInt();
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
		for (int i = 1; i <= n; i++) { // 정점 값이 작은 순서부터 탐색한다는 조건이 있다
			Collections.sort(a[i]);
		}
		c = new boolean[n + 1];
		dfs(start);
		System.out.println();
		c = new boolean[n + 1];
		bfs(start);
		System.out.println();
	}

	public static void 인접행렬_dfs(int x, int n) {
		if (c[x]) {
			return;
		}
		c[x] = true;
		System.out.print(x + " ");
		//연결되고 방문 안된 노드 탐색 (낮은 노드부터 방문됨)
		for (int i = 1; i <= n; i++) {
			if (map[x][i] == 1 && !c[i]) {
				인접행렬_dfs(i, n);
			}
		}
	}

	public static void 인접행렬_bfs(int start, int n) {
		Queue<Integer> q = new LinkedList<>();
		q.add(start);
		c[start] = true;
		System.out.print(start + " ");
		while (!q.isEmpty()) {
			int current = q.remove();
			for (int i = 1; i <= n; i++) {
				if (map[current][i] == 1 && !c[i]) {
					q.add(i);
					c[i] = true;
					System.out.print(i + " ");
				}
			}
		}
	}

	public static void 인접행렬_이용() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int start = sc.nextInt();
		map = new int[n + 1][n + 1];
		for (int i = 1; i <= m; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			map[u][v] = map[v][u] = 1;
		}
		c = new boolean[n + 1];
		인접행렬_dfs(start, n);
		System.out.println();
		c = new boolean[n + 1];
		인접행렬_bfs(start, n);
	}

	public static void main(String[] args) {
		인접리스트_이용();
		인접행렬_이용();
	}
}
