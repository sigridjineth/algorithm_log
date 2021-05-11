import java.util.Scanner;

public class 집합_Q11723 {

	private static final int n = 20;
	private static int s = 0;
	private static StringBuilder sb = new StringBuilder();

	private static void add(int value) {
		int x = value - 1;
		s = (s | (1 << x));
	}

	private static void remove(int value) {
		int x = value - 1;
		s = (s & ~ (1 << x));
	}

	private static void check(int value) {
		int x = value - 1;
		int res = (s & (1 << x));
		if (res == 0) {
			sb.append("0\n");
		} else {
			sb.append("1\n");
		}
	}

	private static void toggle(int value) {
		int x = value - 1;
		s = (s ^ (1 << x));
	}

	private static void all() {
		s = (1 << n) - 1;
	}

	private static void empty() {
		s = 0;
	}


	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int m = Integer.parseInt(sc.nextLine());

		while (m-- > 0) {
			String[] line = sc.nextLine().split(" ");
			String type = line[0];
			if (type.equals("all")) {
				all();
			}
			if (type.equals("empty")) {
				empty();
			}

			if (line.length < 2) {
				continue;
			}

			int value = Integer.parseInt(line[1]);
			if (type.equals("add")) {
				add(value);
			}
			if (type.equals("remove")) {
				remove(value);
			}
			if (type.equals("check")) {
				check(value);
			}
			if (type.equals("toggle")) {
				toggle(value);
			}
		}
		System.out.println(sb);
	}
}
