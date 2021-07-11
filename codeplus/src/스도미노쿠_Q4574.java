import java.util.Arrays;
import java.util.Scanner;

public class 스도미노쿠_Q4574 {
	static int[][] a = new int[10][10];
	static boolean[][][] c = new boolean[3][10][10];
	static boolean[][] domino = new boolean[10][10];
	static final int n = 9;
	static final int[] dx = {0, 1};
	static final int[] dy = {1, 0};
	static int square(int x, int y) {
		return (x / 3) * 3 + (y / 3);
	}
	static boolean can(int x, int y, int num) {
		return !c[0][x][num] && !c[1][y][num] && !c[2][square(x, y)][num];
	}
	static void check(int x, int y, int num, boolean what) {
		c[0][x][num] = what;
		c[1][y][num] = what;
		c[2][square(x, y)][num] = what;
	}
	static boolean check_range(int x, int y) {
		return 0 <= x && x < n && 0 <= y && y < n;
	}
	static boolean go(int z) {
		if (z == 81) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					System.out.print(a[i][j]);
				}
				System.out.println();
			}
			return true;
		}
		int x = z / n;
		int y = z % n;
		if (a[x][y] != 0) {
			return go(z + 1);
		} else if (a[x][y] == 0) {
			for (int k = 0; k < 2; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (!check_range(nx, ny)) {
					continue;
				}
				if (a[nx][ny] != 0) {
					continue;
				}
				for (int i = 1; i <= 9; i++) {
					for (int j = 1; j <= 9; j++) {
						if (i == j) {
							continue;
						}
						if (domino[i][j] || domino[j][i]) {
							continue;
						}
						if (can(x, y, i) && can(nx, ny, j)) {
							check(x, y, i, true);
							check(nx, ny, j, true);
							domino[i][j] = true;
							domino[j][i] = true;
							a[x][y] = i;
							a[nx][ny] = j;
							if (go(z + 1)) {
								return true;
							}
							check(x, y, i, false);
							check(nx, ny, j, false);
							domino[i][j] = false;
							domino[j][i] = false;
							a[x][y] = 0;
							a[nx][ny] = 0;
						}
					}
				}
			}
		}
		return false;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = 1;
		while (true) {
			for (int i = 0; i < 10; i++) {
				Arrays.fill(c[0][i], false);
				Arrays.fill(c[1][i], false);
				Arrays.fill(c[2][i], false);
				Arrays.fill(domino[i], false);
				Arrays.fill(a[i], 0);
			}
			int m = sc.nextInt();
			if (m == 0) {
				break;
			}
			for (int i = 0; i < m; i++) {
				int n1 = sc.nextInt();
				String s1 = sc.next();
				int n2 = sc.nextInt();
				String s2 = sc.next();
				int x1 = s1.charAt(0) - 'A';
				int y1 = s1.charAt(1) - '1';
				int x2 = s2.charAt(0) - 'A';
				int y2 = s2.charAt(1) - '1';
				a[x1][y1] = n1;
				a[x2][y2] = n2;
				domino[n1][n2] = true;
				domino[n2][n1] = true;
				check(x1, y1, n1, true);
				check(x2, y2, n2, true);
			}
			for (int i = 1; i <= 9; i++) {
				String s = sc.next();
				int x = s.charAt(0) - 'A';
				int y = s.charAt(1) - '1';
				a[x][y] = i;
				check(x, y, i, true);
			}
			System.out.println("Puzzle " + tc);
			go(0);
			tc += 1;
		}
	}
}
