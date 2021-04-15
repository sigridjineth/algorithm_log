import java.util.Scanner;

public class Remote_1107 {
	protected static boolean[] broken_remote = new boolean[10];
	protected static int check(int c) {
		if (c == 0) {
			if (broken_remote[0]) {
				return 0;
			}
			return 1;
		}
		int len = 0;
		while (c > 0) {
			if (broken_remote[c % 10]) {
				return 0;
			}
			len += 1;
			c /= 10;
		}
		return len;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		for (int i = 0; i < m; i++) {
			int x = sc.nextInt();
			broken_remote[x] = true;
		}
		int answer = n - 100;
		// 0 ~ 99번 사이인 경우 음수를 양수로 바꾸기
		if (answer < 0) {
			answer = -answer;
		}
		for (int i = 0; i <= 1000000; i++) {
			int c = i;
			int len = check(c);
			if (len > 0) {
				// |c-n| 은 절댓값이어야 하므로 press가 음수이면 양수로 바꿔줘야 한다.
				int press = c - n;
				if (press < 0) {
					press = -press;
				}
				// 최솟값 갱신하기
				if (answer > len + press) {
					answer = len + press;
				}
			}
		}
		System.out.println(answer);
	}
}
