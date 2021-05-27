import java.util.Scanner;

public class 퇴사_Q14501_DP {
	static final int inf = 100000000;
	static int[] t = new int[16];
	static int[] p = new int[16];
	static int[] d = new int[16];
	static int n;

	static int go(int day) {
		if (day == n + 1) {
			return 0;
		}
		if (day > n + 1) {
			return -inf;
		}
		if (d[day] != -1) {
			return d[day];
		}
		int t1 = go(day + 1); // x
		int t2 = p[day] + go(day + t[day]); // o
		d[day] = Math.max(t1, t2);
		return d[day];
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		for (int i = 1; i <= n; i++) {
			t[i] = sc.nextInt();
			p[i] = sc.nextInt();
			d[i] = -1;
		}
		System.out.println(go(1));
	}
}
