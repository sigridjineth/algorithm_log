// 개미전사 문제풀이

solution = () => {
  let n = prompt('정수 N을 입력해주세요.');
  let array = prompt('모든 식량의 정보를 입력해주세요.').split(" ");
  // 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
  let d = new Array(100).fill(0);
  // 첫 번째 선택의 결과는 자기 자신
  d[0] = array[0];
  // 두 번째 선택의 결과는 자기 자신과 첫 번째의 최대
  d[1] = Math.max(parseInt(array[0]), parseInt(array[1]));
  // 점화식을 세워 재귀를 통해 문제를 해결한다
  for (let i = 2; i < n; i++) {
    // (i - 1) 번째 식량창고를 털기로 결정한 경우 현재는 털 수 없다.
    // (i - 2) 번째 식량창고를 털기로 결정한 경우 현재를 털 수 있다.
    d[i] = Math.max(parseInt(d[i - 1]), 
    parseInt(d[i - 2]) + parseInt(array[i]));
  }
  return d[n - 1];
}

solution();
