import java.util.Scanner;

public class candy_3085 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		char[][] array = new char[n][n];
		for (int i = 0; i < n; i++){
			array[i] = sc.next().toCharArray();
		}
		int answer = 0;
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++) {
				// 조건에 맞는 지 먼저 체크하고, 이후에 행을 먼저 검사
				if (j + 1 < n) {
					char original = array[i][j];
					// swap
					array[i][j] = array[i][j+1];
					array[i][j+1] = original;
					int temp = check(array, i, i, j, j+1);
					// 최댓값 갱신
					if (answer < temp) {
						answer = temp;
					}
					// 원래 상태로 복원
					char original_again = array[i][j];
					array[i][j] = array[i][j+1];
					array[i][j+1] = original_again;
				}
				// 조건에 맞는 지 먼저 체크하고, 이후에 열을 검사
				if (i + 1 < n) {
					char original = array[i][j];
					array[i][j] = array[i+1][j];
					array[i+1][j] = original;
					int temp = check(array, i, i+1, j, j);
					if (answer < temp) {
						answer = temp;
					}
					char original_again = array[i][j];
					array[i][j] = array[i+1][j];
					array[i+1][j] = original_again;
				}
			}
		}
		System.out.println(answer);
	}

	private static int check(char[][] array, int start_row, int end_row, int start_col, int end_col) {
		int n = array.length;
		int answer = 1;
		for (int i = start_row; i <= end_row; i++) {
			int count = 1;
			for (int j = 1; j < n; j++) {
				if (array[i][j] == array[i][j-1]) {
					count += 1;
				} else {
					count = 1;
				}
			}
			if (answer < count) {
				answer = count;
			}
		}
		for (int i = start_col; i <= end_col; i++) {
			int count = 1;
			for (int j = 1; j < n; j++) {
				if (array[j][i] == array[j-1][i]) {
					count += 1;
				} else {
					count = 1;
				}
			}
			if (answer < count) {
				answer = count;
			}
		}
		return answer;
	}
}
