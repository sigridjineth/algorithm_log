import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 이모티콘_14226 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] d = new int[n + 1][n + 1];
		for (int i = 0; i < n + 1; i++) {
			Arrays.fill(d[i], -1); // default value is -1
		}
		Queue<Integer> queue = new LinkedList<>();
		queue.add(1);
		queue.add(0);
		d[1][0] = 0;
		while (!queue.isEmpty()) {
			int s = queue.remove();
			int c = queue.remove();
			if (s <= n && d[s][s] == -1) {
				d[s][s] = d[s][c] + 1;
				queue.add(s);
				queue.add(s);
			}
			if (s + c <= n && d[s + c][c] == -1) {
				d[s + c][c] = d[s][c] + 1;
				queue.add(s + c);
				queue.add(c);
			}
			if (s - 1 >= 0 && d[s - 1][c] == -1) {
				d[s - 1][c] = d[s][c] + 1;
				queue.add(s - 1);
				queue.add(c);
			}
		}
		int answer = -1;
		for (int i = 0; i <= n; i++) {
			if (d[n][i] != -1) {
				if (answer == -1 || answer > d[n][i]) {
					answer = d[n][i];
				}
			}
		}
		System.out.println(answer);
	}
}
