import java.util.ArrayList;
import java.util.Scanner;

public class StartAndLink_14889 {
	static int[][] s;
	static int n;
	static int go(int index, ArrayList<Integer> first, ArrayList<Integer> second) {
		if (index == n) {
			if (first.size() != n / 2 || second.size() != n / 2) {
				return -1;
			}
			int a1 = 0;
			int a2 = 0;
			for (int i = 0; i < n / 2; i++) {
				for (int j = 0; j < n / 2; j++) {
					if (i == j) {
						continue;
					}
					a1 += s[first.get(i)][first.get(j)];
					a2 += s[second.get(i)][second.get(j)];
				}
			}
			return Math.abs(a1 - a2);
		}

		int answer = -1;
		first.add(index);
		int a1 = go(index + 1, first, second);
		if (answer == -1 || (a1 != -1 && answer > a1)) {
			answer = a1;
		}
		first.remove(first.size() - 1);

		second.add(index);
		int a2 = go(index + 1, first, second);
		if (answer == -1 || (a2 != -1 && answer > a2)) {
			answer = a2;
		}
		second.remove(second.size() - 1);
		return answer;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		s = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				s[i][j] = sc.nextInt();
			}
		}
		ArrayList<Integer> first = new ArrayList<>();
		ArrayList<Integer> second = new ArrayList<>();
		System.out.println(go(0, first, second));
	}
}
