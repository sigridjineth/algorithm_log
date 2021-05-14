import java.util.Scanner;

public class Q11726_2Xn타일링_탑다운 {
	public static int[] d;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		d = new int[1001];
		System.out.println(go(n));
	}

	public static int go(int n) {
		if (n <= 1) {
			return 1;
		}
		if (d[n] > 0) {
			return d[n];
		}
		d[n] = go(n - 1) + go(n - 2);
		d[n] %= 10007;
		return d[n];
	}
}
