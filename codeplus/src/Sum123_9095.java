import java.util.Scanner;

public class Sum123_9095 {
	static int go(int count, int sum, int goal) {
		if (sum > goal) {
			return 0;
		} else if (sum == goal) {
			return 1;
		}

		int now = 0;
		for (int i = 1; i <= 3; i++) {
			now += go(count + 1, sum + i, goal);
		}
		return now;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();

		while (tc-- > 0) {
			int n = sc.nextInt();
			System.out.println(go(0, 0, n));
		}
	}
}
