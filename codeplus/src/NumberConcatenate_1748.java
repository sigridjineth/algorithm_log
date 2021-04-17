import java.util.Scanner;

public class NumberConcatenate_1748 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int answer = 0;
		for (int start = 1, len = 1; start <= n; start *= 10, len++) {
			int end = start * 10 - 1;
			if (end > n) {
				end = n;
			}
			answer += (end - start + 1) * len;
		}
		System.out.println(answer);
	}
}
