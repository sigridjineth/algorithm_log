public class 카카오2021_광고삽입 {
	static int[] ad = new int[360_001];
	public static void main(String[] args) {
		String play_time = "02:03:55";
		String adv_time = "00:14:15";
		String[] logs = {"01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"};
		System.out.println(solution(play_time, adv_time, logs));
	}
	public static String solution(String play_time, String adv_time, String[] logs) {
		int play_len = timeToInt(play_time);
		int adv_len = timeToInt(adv_time);
		// add all logs into ad & ad[i] = at the time i, shows up accumulated total play time
		for (String log: logs) {
			String[] startAndEndTime = log.split("-");
			int startTime = timeToInt(startAndEndTime[0]);
			int endTime = timeToInt(startAndEndTime[1]);
			for (int i = startTime; i < endTime; i++) {
				ad[i] += 1;
			}
		}
		int max_idx = 0;
		long max_sum = 0;
		long sum = 0;
		// initialization from starting at beginning seconds
		for (int k = 0; k <= adv_len; k++) {
			sum = sum + ad[k];
		}
		max_sum = sum;
		// update by iterating each seconds
		for (int i = adv_len; i <= play_len; i++) {
			int newSecondRecord = ad[i];
			int oldSecondRecord = ad[i - adv_len];
			sum = sum + (newSecondRecord - oldSecondRecord);
			if (sum > max_sum) {
				max_sum = sum;
				max_idx = i - adv_len;
			}
		}
		return timeToString(max_idx);
	}
	static int timeToInt(String time) {
		String[] hmn = time.split(":");
		int timeInSeconds = 0;
		for (int i = 0; i < hmn.length; i++) {
			int element = Integer.parseInt(hmn[i]);
			if (i == 0) {
				timeInSeconds = timeInSeconds + element * 3600;
			} else if (i == 1) {
				timeInSeconds = timeInSeconds + element * 60;
			} else if (i == 2){
				timeInSeconds = timeInSeconds + element;
			}
		}
		return timeInSeconds;
	}

	static String timeToString(int time) {
		StringBuilder t = new StringBuilder();
		int hour = time / 3600;
		time = time % 3600;
		int minute = time / 60;
		time = time % 60;
		int second = time;

		if (hour < 10) {
			t.append("0").append(hour).append(":");
		} else {
			t.append(hour).append(":");
		}
		if (minute < 10) {
			t.append("0").append(minute).append(":");
		} else {
			t.append(minute).append(":");
		}
		if (second < 10) {
			t.append("0").append(second);
		} else {
			t.append(second);
		}
		return t.toString();
	}
}
