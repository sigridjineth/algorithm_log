import java.util.Scanner;

public class NandM4_15652_Recursive {
	static int[] cnt = new int[10];
	static StringBuilder go(int index, int selected, int n, int m) {
		if (selected == m) {
			StringBuilder sb = new StringBuilder();
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= cnt[i]; j++) {
					sb.append(i);
					sb.append(" ");
				}
			}
			sb.append("\n");
			return sb;
		}
		StringBuilder answer = new StringBuilder();
		if (index > n) {
			return answer;
		}
		for (int i = m - selected; i >= 1; i--) {
			cnt[index] = i;
			answer.append(go(index + 1, selected + i, n, m));
		}
		cnt[index] = 0;
		answer.append(go(index + 1, selected, n, m));
		return answer;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		System.out.print(go(1, 0, n, m));
	}
}
