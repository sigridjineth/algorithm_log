import java.util.Scanner;

public class sum123_9095 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] array = new int[11];
		int[] answer = new int[num];
		array[0] = 0;
		array[1] = 1;
		array[2] = 2;
		array[3] = 4;

		int input = 0;
		for (int i = 0; i < num; i++) {
			input = sc.nextInt();
			for (int j = 4; j <= input; j++) {
				array[j] = array[j - 1] + array[j - 2] + array[j - 3];
			}
			answer[i] = array[input];
		}
		for (int i = 0; i < num; i++) {
			System.out.println(answer[i]);
		}
	}
}
