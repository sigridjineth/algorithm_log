import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Query {
	String query;
	List<Integer> scoreList;
	Query(String query) {
		this.query = query;
		scoreList = new ArrayList<>();
	}
	void addScore(int score) {
		scoreList.add(score);
	}
	boolean isMatchedString(String queryString) {
		return query.equals(queryString);
	}
	void sortScore() {
		Collections.sort(scoreList);
	}
}

public class 카카오2021_순위검색 {
	static Set<Query> querySet = new HashSet<>();

	public static void main(String[] args) {
		String[] info1 = {"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"};
		String[] query = {"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"};
		for (String s : info1) {
			dfs("", 0, s.split(" "));
		}
		querySet.forEach(Query::sortScore);
		List<Integer> answerByQuery = new ArrayList<>();
		for (String queryString: query) {
			String[] candidate = queryString.replaceAll(" and ", "").split(" ");
			String queryCondition = candidate[0];
			int score = Integer.parseInt(candidate[1]);
			answerByQuery.add(binarySearch(queryCondition, score));
		}
		Integer[] answer = answerByQuery.toArray(new Integer[query.length]);
		System.out.println(answer);
	}

	static void dfs(String queryString, int depth, String[] info) {
		if (depth == 4) {
			if (querySet.stream().noneMatch(q -> q.isMatchedString(queryString))) {
				Query query = new Query(queryString);
				query.addScore(Integer.parseInt(info[4]));
				querySet.add(query);
			} else {
				querySet.stream()
					.filter(q -> q.isMatchedString(queryString)).findAny().get()
					.addScore(Integer.parseInt(info[4]));
			}
			return;
		}
		dfs(queryString.concat(info[depth]), depth + 1, info);
		dfs(queryString.concat("-"), depth + 1, info);
	}

	static int binarySearch(String queryString, int score) {
		if (querySet.stream().noneMatch(q -> q.isMatchedString(queryString))) {
			return 0;
		}
		List<Integer> scoreList = querySet.stream().filter(q -> q.isMatchedString(queryString))
			.findAny().get().scoreList;
		int start = 0;
		int end = scoreList.size() - 1;
		while (start <= end) {
			int mid = (start + end) / 2;
			if (scoreList.get(mid) < score) {
				start = mid + 1;
			} else {
				end = mid - 1;
			}
		}
		return scoreList.size() - start;
	}
}
