import java.util.Scanner;

public class 가장긴감소하는부분수열_Q11722 {

	public static void main(String[] args) {
		가장_긴_증가하는_부분수열_비슷하게();
		역순으로_가장_긴_증가하는_부분수열();
	}

	public static void 가장_긴_증가하는_부분수열_비슷하게() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n+1];
		int[] d = new int[n+1];
		for (int i=1; i<=n; i++) {
			a[i] = sc.nextInt();
		}
		for (int i=1; i<=n; i++) {
			d[i] = 1;
			for (int j=1; j<=i; j++) {
				if (a[j] > a[i] && d[i] < d[j]+1) {
					d[i] = d[j]+1;
				}
			}
		}
		int ans = d[1];
		for (int i=2; i<=n; i++) {
			if (ans < d[i]) {
				ans = d[i];
			}
		}
		System.out.println(ans);
	}

	public static void 역순으로_가장_긴_증가하는_부분수열() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n+1];
		int[] d = new int[n+1];
		for (int i=1; i<=n; i++) {
			a[i] = sc.nextInt();
		}
		for (int i=n; i>=1; i--) {
			d[i] = 1;
			for (int j=i+1; j<=n; j++) {
				if (a[i] > a[j] && d[i] < d[j]+1) {
					d[i] = d[j]+1;
				}
			}
		}
		int ans = d[1];
		for (int i=2; i<=n; i++) {
			if (ans < d[i]) {
				ans = d[i];
			}
		}
		System.out.println(ans);
	}
}
