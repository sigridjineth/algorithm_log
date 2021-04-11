import java.util.*;

public class Dwarf_2309 {
	public static int NUMBER_OF_GIVEN_DWARFS = 9;
	public static int NUMBER_OF_TRUE_DWARFS = 7;
	public static int TOTAL_DWARFS_HEIGHT = 100;
	public static int GIVEN_DWARFS_HEIGHT_SUM = 0;
	public static int[] GIVEN_DWARFS_HEIGHT;

	public static void main(String[] args) {
		System.out.println("백준 일곱난쟁이 2309 문제입니다.");
		Scanner sc = new Scanner(System.in);
		GIVEN_DWARFS_HEIGHT = new int[NUMBER_OF_GIVEN_DWARFS];
		// get input
		for (int i = 0; i < NUMBER_OF_GIVEN_DWARFS; i++) {
			GIVEN_DWARFS_HEIGHT[i] = sc.nextInt();
			GIVEN_DWARFS_HEIGHT_SUM += GIVEN_DWARFS_HEIGHT[i];
		};
		// sort
		Arrays.sort(GIVEN_DWARFS_HEIGHT);
		// iteration
		for (int i = 0; i < NUMBER_OF_GIVEN_DWARFS; i++){
			for (int j = i + 1; j < NUMBER_OF_GIVEN_DWARFS; j++) {
				if (GIVEN_DWARFS_HEIGHT_SUM - GIVEN_DWARFS_HEIGHT[i] - GIVEN_DWARFS_HEIGHT[j] == TOTAL_DWARFS_HEIGHT) {
					// i와 j를 제외하고 출력한다
					print(i, j);
				}
			}
		}
	}

	public static void print(int first_element, int second_element) {
		for (int i = 0; i < NUMBER_OF_TRUE_DWARFS + 1; i++) {
			if (i == first_element || i == second_element) {
				continue;
			}
			System.out.println(GIVEN_DWARFS_HEIGHT[i]);
		}
	}
}