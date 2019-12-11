function solution(numbers, target){
    let answer = 0;
    dfs(0);
    
    function dfs(k){
        if (k === numbers.length){
            let sum = 0;
            for (let num of numbers){
                sum += num;
            };
            if (sum === target){
                return answer++;
            };
        } else {
            numbers[k] *= 1;
			dfs(k+1);
			numbers[k] *= -1;
			dfs(k+1);
        }
    }
	return answer;
};
//고생 끝에 나름 이해했지만 여전히 어려운 개념이다.
//DFS, BFS에 대해 추가로 학습하기로 한다.
//참고한 링크는 https://new93helloworld.tistory.com/358, https://spoit.tistory.com/14 이다. 