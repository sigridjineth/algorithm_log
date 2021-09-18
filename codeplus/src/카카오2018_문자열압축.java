public class 카카오2018_문자열압축 {
	public static void main(String[] args) {
		String s = "ababcdcdababcdcd";
		System.out.println(solution(s));
	}
	public static int solution(String s) {
		String answer = s;
		int MAX_CUT_LENGTH = s.length() / 2;
		int STR_LENGTH = s.length();
		for (int i = 1; i < MAX_CUT_LENGTH; i++) {
			int count = 0;
			StringBuilder temp_str = new StringBuilder();
			String bench_str = s.substring(0, i);
			for (int j = i; j < STR_LENGTH; j += i) {
				String str = s.substring(j, j + i);
				if (bench_str.equals(str)) {
					count += 1;
				} else {
					if (count > 1) {
						temp_str.append(count).append(bench_str);
					} else {
						temp_str.append(bench_str);
					}
					bench_str = str;
					count = 1;
				}
			}
			if (answer.length() > temp_str.length()) {
				answer = temp_str.toString();
			}
		}
		return answer.length();
	}
}
