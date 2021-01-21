// Group Anagrams Leetcode #49

solution = (strs) => {
    const groups = {} // object 생성
    for (let i = 0; i < strs.length; i++) {
        let sort = strs[i].split('').sort().join('') // 애너그램 판단 시 정렬하여 비교한다.
        // 단어를 정렬하면 같은 값을 갖게 된다.

        // 만약 존재하지 않으면, object에 Key로 추가
        if (!groups[sort]) {
            groups[sort] = [strs[i]] // if the value is not an array, should wrap the value of keys in brackets.
        } else {
            groups[sort].push(strs[i])
        }
    }

    // 파라미터가 가지는 열거 가능한 키의 값들로 구성된 배열을 반환한다.
    return Object.values(groups)
}