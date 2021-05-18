import java.util.Scanner;

class Q11052_카드구매하기_2 {

	static int[] d;
	static int[] a;

	static int getMaxPrice(int n) {
		if (n == 0) {
			return 0;
		} else if (d[n] > 0) {
			return d[n];
		}
		for (int i = 1; i <= n; i++) {
			d[n] = Math.max(d[n], getMaxPrice(n - i)+ a[i]);
		}
		return d[n];
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		a = new int[n + 1];
		for (int i = 1; i <= n; i++) {
			a[i] = sc.nextInt();
		}
		d = new int[n + 1];
		System.out.println(getMaxPrice(n));
	}
}

public class Q11052_카드구매하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n + 1];
		for (int i = 1; i <= n; i++) {
			a[i] = sc.nextInt();
		}
		int[] d = new int[n + 1];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= i; j++) {
				if (d[i] < d[i - j] + a[j]) {
					d[i] = d[i - j] + a[j];
				}
			}
		}
		System.out.println(d[n]);
	}
}
