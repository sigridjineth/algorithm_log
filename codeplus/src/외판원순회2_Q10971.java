import java.util.Scanner;

public class 외판원순회2_Q10971 {
	public static int answer = Integer.MAX_VALUE;

	private static boolean next_permutation(int[] a) {
		int i = a.length - 1;
		while (i > 0 && a[i-1] >= a[i]) {
			i -= 1;
		}
		if (i <= 0) {
			return false;
		}

		int j = a.length - 1;
		while (a[i-1] >= a[j]) {
			j -= 1;
		}

		int temp = a[i-1];
		a[i-1] = a[j];
		a[j] = temp;

		j = a.length - 1;
		while (i < j) {
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
			i += 1;
			j -= 1;
		}
		return true;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] a = new int[n][n];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				a[i][j] = sc.nextInt();
			}
		}

		int[] d = new int[n];
		for (int i = 0; i < n; i++) {
			d[i] = i;
		}

		do {
			if (d[0] != 0) {
				break;
			}
			boolean not_zero = true;
			int sum = 0;
			for (int i = 0; i < n - 1; i++) {
				if (a[d[i]][d[i+1]] == 0) {
					not_zero = false;
				} else {
					sum += a[d[i]][d[i+1]];
				}
			}
			if (not_zero && a[d[n-1]][d[0]] != 0) {
				sum += a[d[n-1]][d[0]];
				if (answer > sum) {
					answer = sum;
				}
			}
		} while (next_permutation(d));
		System.out.println(answer);
	}
}
