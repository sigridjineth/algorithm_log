import java.util.Arrays;
import java.util.Scanner;

public class 로또_Q6603_재귀함수식풀이 {
	public static int k;
	public static int[] arr;
	public static boolean[] choose;

	private static void dfs(int count, int index) {
		if (count == 6) {
			for (int i = 0; i < k; i++) {
				if (choose[i] == true) {
					System.out.print(arr[i] + " ");
				}
			}
			System.out.println();
		}

		for (int j = index; j < k; j++) {
			choose[j] = true;
			dfs(count + 1, j + 1);
			choose[j] = false;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			k = sc.nextInt();
			if (k == 0) {
				break;
			}
			arr = new int[k];
			choose = new boolean[k];
			for (int i = 0; i < arr.length; i++) {
				arr[i] = sc.nextInt();
			}
			Arrays.sort(arr);
			dfs(0, 0);
			System.out.println();
		}
		sc.close();
	}
}
