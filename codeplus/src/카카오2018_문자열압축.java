public class 카카오2018_문자열압축 {
	public static void main(String[] args) {
		String s = "abcabcdede";
		System.out.println(solution(s));
	}
	public static String solution(String s) {
		String answer = s;
		int MAX_CUT_LENGTH = s.length() / 2;
		int STR_LENGTH = s.length();
		for (int i = 1; i < MAX_CUT_LENGTH + 1; i++) {
			int count = 1;
			StringBuilder temp_str = new StringBuilder();
			String bench_str = s.substring(0, i);
			for (int j = i; j < STR_LENGTH; j += i) {
				StringBuilder sub = new StringBuilder();
				for (int k = j; k < j + i; k++) {
					if (k < STR_LENGTH) {
						sub.append(s.charAt(k));
					}
				}
				if (bench_str.equals(sub.toString())) {
					count += 1;
				} else {
					if (count > 1) {
						temp_str.append(count).append(bench_str);
					} else {
						temp_str.append(bench_str);
					}
					bench_str = sub.toString();
					count = 1;
				}
			}
			if (count > 1) {
				temp_str.append(count).append(bench_str);
			} else {
				temp_str.append(bench_str);
			}
			if (answer.length() > temp_str.length()) {
				answer = temp_str.toString();
			}
		}
		return answer;
	}
}
