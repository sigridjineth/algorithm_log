import java.util.Scanner;

public class 제곱수의합_Q1699 {
	private static final int[] d = new int[100001];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		for (int i = 1; i <= n; i++) {
			// 최대값을 초기값으로 넣어 줌. 1을 i번 하면 최댓값이기 때문.
			d[i] = i;
			for (int j = 1; j * j <= i; j++) {
				if (d[i] > d[i - (j * j)] + 1) {
					d[i] = d[i - (j * j)] + 1;
				}
			}
		}
		System.out.println(d[n]);
	}
}
