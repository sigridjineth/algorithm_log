// String Manipulation, Leetcode 125
// 리스트로 변환하는 방식 차용. 속도는 느리다.

solution = (str) => {
    array = []
    str.split("").map((element) => {
        if (/[a-zA-Z0-9]/.test(element)) {
            array.push(element.toLowerCase())
        }
    });

    while (array.length > 1) {
        if (array.pop() != array.shift()) {
            return false
        }
    }
    return true
}

// deque 라이브러리를 직접 구현하여 풀이하는 방식을 추가해보자.