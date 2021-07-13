import java.util.Scanner;

public class 가르침_Q1062 {
	static int count(int mask, int[] words) {
		int cnt = 0;
		for (int word: words) {
			if ((word & ((1 << 26) - 1 - mask)) == 0) {
				cnt += 1;
			}
		}
		return cnt;
	}
	static int go(int index, int k, int mask, int[] words) {
		if (k < 0) {
			return 0;
		}
		if (index == 26) {
			return count(mask, words);
		}
		int ans = 0;
		// 고르는 경우
		int t1 = go(index + 1, k - 1, mask | (1 << index), words);
		if (ans < t1) {
			ans = t1;
		}
		if (index != 'a' - 'a' && index != 'n' - 'a' && index != 't' - 'a' && index != 'i' - 'a' && index != 'c' - 'a') {
			t1 = go(index + 1, k, mask, words);
			if (ans < t1) {
				ans = t1;
			}
		}
		return ans;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] words = new int[n];
		for (int i = 0; i < n; i++) {
			String s = sc.next();
			for (char x: s.toCharArray()) {
				words[i] |= (1 << (x - 'a'));
			}
		}
		System.out.println(go(0, m, 0, words));
	}
}
