import java.util.Scanner;

public class Q1248_맞춰봐 {

	static int n;
	static int[][] sign;
	static int[] answer;

	static boolean check(int index) {
		int sum = 0;
		for (int i = index; i >= 0; i--) {
			sum += answer[i];
			if (sign[i][index] == 0) {
				if (sum != 0) {
					return false;
				}
			}
			if (sign[i][index] > 0) {
				if (sum <= 0) {
					return false;
				}
			}
			if (sign[i][index] < 0) {
				if (sum >= 0) {
					return false;
				}
			}
		}
		return true;
	}

	static boolean go(int index) {
		if (index == n) {
			return true;
		}
		if (sign[index][index] == 0) {
			answer[index] = 0;
 			return check(index) && go(index + 1);
		}
		for (int i = 1; i <= 10; i++){
			answer[index] = sign[index][index] * i;
			if (check(index) && go(index + 1)) {
				return true;
			}
		}
		return false;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		answer = new int[n];
		sign = new int[n][n];

		String s = sc.next();
		int cnt = 0;

		for (int i = 0; i < n; i++) {
			for (int j = i; j < n; j++) {
				char x = s.charAt(cnt);
				if (x == '0') {
					sign[i][j] = 0;
				}
				if (x == '+') {
					sign[i][j] = 1;
				}
				if (x == '-') {
					sign[i][j] = -1;
				}
				cnt += 1;
			}
		}

		go(0);
		for (int i = 0; i < n; i++) {
			System.out.println(answer[i] + " ");
		}
		System.out.println();
	}
}
