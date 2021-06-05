import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 연결요소_Q11724 {
	static ArrayList<Integer>[] a;
	static ArrayList<ArrayList<Integer>> list;
	static boolean[] c;

	public static void dfs(int x) {
		if (c[x]) {
			return;
		}
		c[x] = true;
		for (int y : a[x]) {
			if (!c[y]) {
				dfs(y);
			}
		}
	}

	public static void dfs식_풀이() {
		Scanner sc = new Scanner(System.in);
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
		c = new boolean[n + 1];
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			if (!c[i]) {
				dfs(i);
				ans += 1;
			}
		}
		System.out.println(ans);
	}

	public static void bfs(int n) {
		Queue<Integer> queue = new LinkedList<>();
		queue.add(n);
		while (!queue.isEmpty()) {
			int data = queue.poll();
			c[data] = true;
			for (int i = 0; i < list.get(data).size(); i++) {
				int result = list.get(data).get(i);
				if (!c[result]) {
					c[result] = true;
					queue.add(result);
				}
			}
		}
	}

	public static void bfs식_풀이() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		c = new boolean[n + 1];
		list = new ArrayList<>();
		for (int i = 0; i < n + 1; i++) {
			list.add(new ArrayList<>());
		}
		for (int i = 0; i < m; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			list.get(u).add(v);
			list.get(v).add(u);
		}
		int count = 0;
		for (int i = 1; i < n + 1; i++) {
			if (!c[i]) {
				bfs(i);
				count += 1;
			}
		}
		System.out.println(count);
	}

	public static void main(String[] args) {
		dfs식_풀이();
		bfs식_풀이();
	}
}
