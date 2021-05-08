import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class 로또_Q6603_순열식풀이 {
	private static boolean next_permutation(int[] a) {
		int i = a.length - 1;
		while (i > 0 && a[i-1] >= a[i]) {
			i -= 1;
		}
		if (i <= 0) {
			return false;
		}
		int j = a.length - 1;
		while (a[j] <= a[i-1]) {
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
		while (true) {
			int n = sc.nextInt();
			if (n == 0) {
				break;
			}
			int[] a = new int[n];
			for (int i = 0; i < n; i++) {
				a[i] = sc.nextInt();
			}
			int[] d = new int[n];
			for (int i = 0; i < n; i++) {
				if (i < n - 6) {
					d[i] = 0; // (n - 6) 보다 작은 값은 0으로, 나머지 큰 값은 1로 초기값 세팅
				} else {
					d[i] = 1;
				}
			}

			ArrayList<ArrayList<Integer>> answer = new ArrayList<>();
			do {
				ArrayList<Integer> cur = new ArrayList<>();
				for (int i = 0; i < n; i++) {
					if (d[i] == 1) {
						cur.add(a[i]);
					}
				}
				answer.add(cur);
			} while (next_permutation(d));

			Collections.sort(answer, new Comparator<ArrayList<Integer>>() {
				@Override
				public int compare(ArrayList<Integer> o1, ArrayList<Integer> o2) {
					int n = o1.size();
					int m = o2.size();
					int i = 0;

					while (i < n && i < m) {
						int t1 = o1.get(i);
						int t2 = o2.get(i);
						if (t1 < t2) {
							return -1;
						} else if (t1 > t2) {
							return 1;
						}
						i += 1;
					}

					if (i == n && i != m) {
						return -1;
					} else if (i != n && i == m) {
						return 1;
					} else {
						return 0;
					}
				}
			});

			for (ArrayList<Integer> v : answer) {
				for (int x : v) {
					System.out.print(x + " ");
				}
				System.out.println();
			}
			System.out.println();
		}
	}
}
