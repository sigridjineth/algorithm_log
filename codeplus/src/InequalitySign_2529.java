import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class InequalitySign_2529 {

	private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static int N;
	private static final char[] arr = new char[10];
	private static final boolean[] visited = new boolean[10];
	private static final ArrayList<String> answer = new ArrayList<>();

	private static void dfs(String num, int idx) {
		if (idx == N + 1) {
			answer.add(num);
		}

		for (int i = 0; i <= 9; i++) {
			if (visited[i]) {
				continue;
			}
			if (idx == 0 || good(Integer.parseInt(String.valueOf(num.charAt(idx - 1))), i, arr[idx - 1])) {
				visited[i] = true;
				dfs(num + i, idx + 1);
				visited[i] = false;
			}
		}
	}

	private static boolean good(int x, int y, char op) {
		if (op == '<') {
			if (x > y) {
				return false;
			}
		}
		if (op == '>') {
			return x >= y;
		}
		return true;
	}

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < N; i++) {
			arr[i] = st.nextToken().charAt(0);
		}

		dfs("", 0);
		Collections.sort(answer);

		System.out.println(answer.get(answer.size() - 1));
		System.out.println(answer.get(0));
		br.close();
	}
}
