import java.util.Scanner;

public class Tetromino_14500 {
	static String[][] blocks = {
		{"1111"},
		{"11", "11"},
		{"10", "10", "11"},
		{"111", "010"},
		{"10", "11", "01"}
	};

	static String[] mirror(String[] input) {
		String[] answer = new String[input.length];
		for (int i = 0; i < input.length; i++) {
			answer[i] = new StringBuilder(input[i]).reverse().toString();
		}
		return answer;
	}

	static String[] rotate(String[] input) {
		String[] answer = new String[input[0].length()];
		for (int i = 0; i < input[0].length(); i++) {
			StringBuilder sb = new StringBuilder();
			for (int j = input.length - 1; j >= 0; j--) {
				sb.append(input[j].charAt(i));
			}
			answer[i] = sb.toString();
		}
		return answer;
	}

	public static int calculate(int[][] array, String[] temp, int starting_x, int starting_y) {
		int n = array.length;
		int m = array[0].length;
		int sum = 0;
		for (int i = 0; i < temp.length; i++) {
			for (int j = 0; j < temp[0].length(); j++) {
				if (temp[i].charAt(j) == '0') {
					continue;
				}
				int nx = starting_x + i;
				int ny = starting_y + j;
				if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
					sum += array[nx][ny];
				} else {
					return -1;
				}
			}
		}
		return sum;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] line = sc.nextLine().split(" ");
		int n = Integer.parseInt(line[0]);
		int m = Integer.parseInt(line[1]);
		int[][] array = new int[n][m];
		for (int i = 0; i < n; i++) {
			String[] row = sc.nextLine().split(" ");
			for (int j = 0; j < m; j++) {
				array[i][j] = Integer.parseInt(row[j]);
			}
		}
		int answer = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				for (String[] block: blocks) {
					String[] temp = new String[block.length];
					System.arraycopy(block, 0, temp, 0, block.length);
					for (int mirror = 0; mirror < 2; mirror++) {
						for (int rotate = 0; rotate < 4; rotate++) {
							int current = calculate(array, temp, i, j);
							if (current != -1 && answer < current) {
								answer = current;
							}
							temp = rotate(temp);
						}
						temp = mirror(temp);
					}
				}
			}
		}
		System.out.println(answer);
	}
}
