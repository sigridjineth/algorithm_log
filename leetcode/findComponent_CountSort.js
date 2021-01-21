// 부품 찾기 문제를 계수 정렬로 문제 풀이

solution = () => {
  let n = prompt('가게의 부품 개수 입력');
  // 계수 정렬을 위해 전체 리스트 초기화
  let initSize = 1000001;
  let array = [...Array(n)].map((item, index, array) => 0);
  // 가게에 있는 전체 부품 번호 입력받아서 기록
  let storeStock = prompt('가게 전체 부품 번호 입력').split(" ");
  for (let i of storeStock) {
    array[i] = 1;
  }
  // 손님이 확인 요청한 부품 개수 입력
  let m = prompt('손님 요청한 부품 개수 입력');
  // 손님이 확인 요청한 전체 부품 번호 입력
  reducer = (acc, value) => {
    acc.push(Number(value));
    return acc;
  }
  let initialValue = [];
  let guestRequest = prompt('손님 확인 요청한 전체 부품 번호 입력').split(" ").reduce(reducer, initialValue);
  console.log(guestRequest);
  console.log(storeStock);
  // 손님이 확인 요청한 부품 번호를 하나씩 확인
  for (let i of guestRequest) {
    if (array[i] == 1) {
      console.log('yes', " ");
    } else {
      console.log('no', " ");
    }
  }
}

solution();
