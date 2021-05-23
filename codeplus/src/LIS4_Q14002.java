import java.util.Scanner;

public class LIS4_Q14002 {

	static int[] a;
	static int[] d;
	static int[] v;
	static void go(int p) {
		if (p == -1) return;
		go(v[p]);
		System.out.print(a[p] + " ");
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		d = new int[n];
		v = new int[n];
		for (int i = 0; i < n; i++) {
			d[i] = 1;
			v[i] = -1;
			for (int j = 0; j < i; j++) {
				if (a[j] < a[i] && d[i] < d[j] + 1) {
					d[i] = d[j] + 1;
					v[i] = j;
				}
			}
		}
		int answer = d[0];
		int p = 0;
		for (int i = 0; i < n; i++) {
			if (answer < d[i]) {
				answer = d[i];
				p = i;
			}
		}
		System.out.println(answer);
		go(p);
		System.out.println();
	}
}
