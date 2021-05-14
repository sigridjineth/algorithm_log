import java.util.Scanner;

public class Q11726_2Xn타일링 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] d = new int[1001];
		d[0] = 1;
		d[1] = 1; // 2 X 1 타일일 때 경우의 수는 1이다.
		for (int i = 2; i <= n; i++) {
			d[i] = d[i - 1] + d[i - 2];
			d[i] %= 10007;
		}
		System.out.println(d[n]);
	}
}
