import java.util.Scanner;

public class KaingCalendar_6064 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = Integer.parseInt(sc.nextLine());
		int[] answer = new int[t];
		for (int i = 0; i < t; i++) {
			String[] line = sc.nextLine().split(" ");
			int m = Integer.parseInt(line[0]);
			int n = Integer.parseInt(line[1]);
			int x = Integer.parseInt(line[2]) - 1;
			int y = Integer.parseInt(line[3]) - 1;

			boolean ok = false;
			for (int k = x; k < (n * m); k += m) {
				if (k % n == y) {
					answer[i] = k + 1;
					ok = true;
					break;
				}
			}
			if (!ok) {
				answer[i] = -1;
			}
		}
		for (int i = 0; i < t; i++) {
			System.out.println(answer[i]);
		}
	}
}
