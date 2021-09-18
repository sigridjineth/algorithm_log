import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class 카카오2019_오픈채팅방 {
	public static void main(String[] args) {
		String[] record = {
		"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
		System.out.println(solution(record));
	}
	private static String[] solution(String[] record) {
		ArrayList<String> chatLog = new ArrayList<>();
		HashMap<String, String> uidToNicknameMap = new HashMap<>();
		for (String log: record) {
			StringTokenizer stringTokenizer = new StringTokenizer(log);
			String command = stringTokenizer.nextToken();
			String userId = stringTokenizer.nextToken();
			String nickname = "";
			if (!command.equals("Leave")) {
				nickname = stringTokenizer.nextToken();
			}
			if (command.equals("Enter")) {
				uidToNicknameMap.put(userId, nickname);
				chatLog.add(userId + "님이 들어왔습니다.");
			}
			if (command.equals("Change")) {
				uidToNicknameMap.put(userId, nickname);
			}
			if (command.equals("Leave")) {
				chatLog.add(userId + "님이 나갔습니다.");
			}
		}
		String[] answer = new String[chatLog.size()];
		int logIndex = 0;
		for (String str: chatLog) {
			int idEndIndex = str.indexOf("님");
			String userId = str.substring(0, idEndIndex);
			answer[logIndex] = str.replace(userId, uidToNicknameMap.get(userId));
			logIndex += 1;
		}
		return answer;
	}
}
