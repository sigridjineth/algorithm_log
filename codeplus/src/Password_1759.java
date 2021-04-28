import java.util.Arrays;
import java.util.Scanner;

public class Password_1759 {
	public static boolean check(String password) {
		int con = 0;
		int vow = 0;

		for (char x : password.toCharArray()) {
			if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') {
				vow += 1;
			} else {
				con += 1;
			}
		}

		return con >= 2 && vow >= 1;
	}

	public static void go(int n, String[] alpha, String password, int i) {
		if (password.length() == n) {
			if (check(password)) {
				System.out.println(password);
			}
			return;
		}
		if (alpha.length <= i) {
			return;
		}

		go(n, alpha, password + alpha[i], i + 1);
		go(n, alpha, password, i + 1);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] lc = sc.nextLine().split(" ");
		int l = Integer.parseInt(lc[0]);
		int m = Integer.parseInt(lc[1]);
		String[] alpha = sc.nextLine().split(" ");

		Arrays.sort(alpha);
		go(l, alpha, "", 0);
	}
}
