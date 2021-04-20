import java.util.Scanner;

public class NandM4_15652 {
	// 선택의 방법 쓰기
	static boolean[] c = new boolean[10];
	static int[] a = new int[10];
	static void go(int index, int start, int n, int m) {
		if (index == m) {
			for (int i = 0; i < m; i++) {
				System.out.print(a[i]);
				System.out.print(" ");
			}
			System.out.println();
			return;
		}
		for (int i = start; i <= n; i++) {
			// 중복을 허락하지 않는 코드
			// if (c[i]) = continue;
			c[i] = true;
			a[index] = i;
			go(index + 1, i, n, m);
			c[i] = false;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		go(0, 1, n, m);
	}
}
