import java.util.Scanner;

public class 부분수열의합_Q1182 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] line = sc.nextLine().split(" ");
		int n = Integer.parseInt(line[0]);
		int s = Integer.parseInt(line[1]);
		int[] a = new int[n];
		String[] values = sc.nextLine().split(" ");

		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(values[i]);
		}

		int answer = 0;
		for (int i = 1; i < (1 << n); i++) {
			int sum = 0;
			for (int j = 0; j < n; j++) {
				if ((i & (1 << j)) != 0) {
					sum += a[j];
				}
			}
			if (sum == s) {
				answer += 1;
			}
		}
		System.out.println(answer);
	}
}
