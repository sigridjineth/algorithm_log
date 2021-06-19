import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 숨바꼭질3_Q13549 {
	public static final int MAX = 200001;

	public static void 큐두개를_사용한다() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] c = new boolean[MAX];
		int[] d = new int[MAX];
		c[n] = true;
		d[n] = 0;
		Queue<Integer> current_queue = new LinkedList<>();
		Queue<Integer> next_queue = new LinkedList<>();
		current_queue.add(n);

		while (!current_queue.isEmpty()) {
			int now = current_queue.remove();
			for (int next: new int[]{now * 2, now - 1, now + 1}) {
				if (next >= 0 && next < MAX) {
					if (!c[next]) {
						c[next] = true;
						if (next == now * 2) {
							current_queue.add(next);
							d[next] = d[now];
						} else {
							next_queue.add(next);
							d[next] = d[now] + 1;
						}
					}
				}
			}

			if (current_queue.isEmpty()) {
				current_queue = next_queue;
				next_queue = new LinkedList<>();
			}
		}

		System.out.println(d[m]);
	}

	public static void Deque을_사용한다() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] c = new boolean[MAX];
		int[] d = new int[MAX];
		c[n] = true;
		d[n] = 0;
		ArrayDeque<Integer> queue = new ArrayDeque<>();
		queue.add(n);

		while (!queue.isEmpty()) {
			int now = queue.poll();
			for (int next: new int[]{now * 2, now - 1, now + 1}) {
				if (next >= 0 && next < MAX) {
					if (!c[next]) {
						c[next] = true;
						if (next == now * 2) {
							queue.addFirst(next);
							d[next] = d[now];
						} else {
							queue.addLast(next);
							d[next] = d[now] + 1;
						}
					}
				}
			}
		}

		System.out.println(d[m]);
	}

	public static void main(String[] args) {
		큐두개를_사용한다();
		Deque을_사용한다();
	}
}
