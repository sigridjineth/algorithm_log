import java.util.Arrays;
import java.util.Scanner;

public class 차이를최대로_Q10819 {
	public static boolean next_permutation(int[] a) {
		int i = a.length - 1;
		while (i > 0 && a[i-1] >= a[i]) {
			i -= 1;
		}
		if (i <= 0) {
			return false;
		}

		int j = a.length - 1;
		while (a[j] <= a[i - 1]) {
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

	public static int calculate(int[] a) {
		int sum = 0;
		for (int i = 1; i < a.length; i++) {
			sum += Math.abs(a[i] - a[i - 1]);
		}
		return sum;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		// next permutation 알고리즘이라는 컨셉 자체가 i와 j 를 찾는 것이 대소 비교를 하며 swap 연산을 하기 때문에 정렬이 순열의 결과에 매우 큰 영향을 미치게 된다.
		Arrays.sort(a);
		int answer = 0;
		do {
			int temp = calculate(a);
			answer = Math.max(answer, temp);
		} while (next_permutation(a));

		System.out.println(answer);
	}
}
