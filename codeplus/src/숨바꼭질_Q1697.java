import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 숨바꼭질_Q1697 {
	public static final int MAX = 200000;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] check = new boolean[MAX];
		int[] dist = new int[MAX];

		check[n] = true;
		dist[n] = 0;
		Queue<Integer> queue = new LinkedList<>();
		queue.add(n);

		while (!queue.isEmpty()) {
			int now = queue.remove();
			if (now - 1 >= 0) {
				if (!check[now - 1]) {
					queue.add(now - 1);
					check[now - 1] = true;
					dist[now - 1] = dist[now] + 1;
				}
			}
			if (now + 1 < MAX) {
				if (!check[now + 1]) {
					queue.add(now + 1);
					check[now + 1] = true;
					dist[now + 1] = dist[now] + 1;
				}
			}
			if (now * 2 < MAX) {
				if (!check[now * 2]) {
					queue.add(now * 2);
					check[now * 2] = true;
					dist[now * 2] = dist[now] + 1;
				}
			}
		}
		System.out.println(dist[m]);
	}
}
