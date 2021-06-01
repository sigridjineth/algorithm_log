import java.util.Scanner;

public class 타일채우기_Q2133 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] d = new long[31];
		d[0] = 1;
		d[2] = 3;

		for (int i = 4; i <= n; i++) {
			d[i] = d[i - 2] * 3;
			for (int j = 4; j <= i; j += 2) {
				d[i] += d[i - j] * 2;
			}
		}
		System.out.println(d[n]);
	}
}
