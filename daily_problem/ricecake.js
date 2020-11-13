// 떡볶이 떡 만들기를 이진 탐색으로 풀이함

solution2 = () => {
  let nm = window.prompt('떡의 개수와 떡의 길이를 입력하시오.').split(" ");
  let n = nm[0];
  let m = nm[1];
  let height = window.prompt('각 떡의 개별 높이 정보를 입력하시오.').split(" ");

  // 이진 탐색을 위한 시작점과 끝점 설정
  let start = 0;
  let end = Math.max.apply(null, height);

  // 이진 탐색 수행(반복적)
  let result = 0;
  // start > end이라면 이진 탐색의 조건 종료 후 정답기대 가능
  while (start <= end) {
    let total = 0;
    let mid = Math.floor((start + end) / 2);
    for (let h of height) {
      // 잘랐을 때의 떡의 양 계산
      if (h > mid) {
        total = total + (h - mid);
      };
    };
    // 떡의 양이 부족한 경우 더 많이 자르기(끝점 줄이기)
    if (total < m) {
      end = mid - 1
    } else {
      // 떡의 양이 넘치는 경우 덜 자르기(시작점 늘이기)
      result = mid; // 최대한 덜 잘랐을 경우가 정답
      start = mid + 1;
    }
  }
  return result;
}

solution2();
