import java.util.*;

public class 숨바꼭질4_Q13913 {
	public static final int MAX = 200000;
	static void print(int[] from, int n, int m) {
		if (n != m) {
			print(from, n, from[m]);
		}
		System.out.print(m + " ");
	}
	static void printWithStack(int[] from, int n, int m) {
		Stack<Integer> ans = new Stack<>();
		for (int i = m; i != n; i=from[i]) {
			ans.push(i);
		}
		ans.push(n);
		while (!ans.isEmpty()) {
			System.out.print(ans.pop() + " ");
		}
	}
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] check = new boolean[MAX];
		int[] dist = new int[MAX];
		int[] from = new int[MAX];
		check[n] = true;
		dist[n] = 0;
		Queue<Integer> q = new LinkedList<>();
		q.add(n);
		while (!q.isEmpty()) {
			int now = q.remove();
			if (now - 1 >= 0) {
				if (!check[now - 1]) {
					q.add(now - 1);
					check[now - 1] = true;
					dist[now - 1] = dist[now] + 1;
					from[now - 1] = now;
				}
			}
			if (now + 1 < MAX) {
				if (!check[now + 1]) {
					q.add(now + 1);
					check[now + 1] = true;
					dist[now + 1] = dist[now] + 1;
					from[now + 1] = now;
				}
			}
			if (now * 2 < MAX) {
				if (!check[now * 2]) {
					q.add(now * 2);
					check[now * 2] = true;
					dist[now * 2] = dist[now] + 1;
					from[now * 2] = now;
				}
			}
		}
		System.out.println(dist[m]);
		print(from, n, m);
		System.out.println();
	}
}
