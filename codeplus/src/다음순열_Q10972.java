import java.util.Scanner;

public class 다음순열_Q10972 {
	public static boolean next_permutation(int[] a) {
		int i = a.length - 1;
		while (i >= 0 && a[i-1] >= a[i]) {
			i -= 1;
		}
		if (i <= 0) {
			return false;
		}

		int j = a.length - 1;
		while (a[j] <= a[i-1]) {
			j -= 1;
		}

		int temp = a[i - 1];
		a[i - 1] = a[j];
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
		int[] a = new int[n];

		for (int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}

		if (next_permutation(a)) {
			StringBuilder answer = new StringBuilder();
			for (int i = 0; i < n; i++) {
				answer.append(a[i]).append(" ");
			}
			System.out.println(answer.toString());
			System.out.println();
		} else {
			System.out.println(-1);
		}
	}
}
