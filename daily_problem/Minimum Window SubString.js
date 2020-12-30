// LEETCODE 76 Minimum Window Substring
// 모든 윈도우 크기를 브루트 포스로 탐색하는 방법이지만, O(n^2)가 소모되어 timeout 된다.
let minWindow_timeOut = function(s, t) {
    function contains(s_substr_lst, t_lst) {
        for (let t_elem of t_lst) {
            if (s_substr_lst.includes(t_elem)) {
                let index = s_substr_lst.indexOf(t_elem)
                s_substr_lst = s_substr_lst.slice(0, index) + s_substr_lst.slice(index + 1, s_substr_lst.length)
            } else {
                return false
            }
        }
        return true
    }
    if (!s || !t) {
        return ''
    }
    let window_size = t.length
    for (let size = window_size; size < s.length + 1; size++) {
        for (let left = 0; left < s.length - size + 1; left++) {
            let s_substr = s.slice(left, left + size)
            if (contains(s_substr, t)) {
                return s_substr
            }
        }
    }
    return ''
};

class Collections {
    counter(array) {
        var count = {}
        array.forEach(val => count[val] = (count[val] || 0) + 1)
        return count
    }
}

// 이런 유형의 문제는 투 포인터와 슬라이딩 윈도우를 함께 사용하면 O(n)으로 줄일 수 있다.
minWindow = (s, t) => {
    let need = new Collections().counter(t.split(""))
    let missing = t.length
    let left = 0
    let start = 0
    let end = 0

    // 오른쪽 포인터 이동
    for (let element of s.split("").entries()) {
        let right = element[0]
        let char = element[1]
        if (right === 0) {
            continue; // 슬라이싱을 위하여 첫 번째 원소는 무시한다.
        }
        missing -= (need[char] > 0) // missing -= 1 when need.char > 0
        need[char] -= 1
        if (missing === 0) {
            while (left < right && need[s[left]] < 0) {
                need[s[left]] += 1
                left += 1
            }
            if (!end || (right - left) <= (end - start)) {
                start = left
                end = right
            }
            need[s[left]] += 1
            missing += 1
            left += 1
        }
    }
    return s.slice(start, end)
}

console.log(minWindow("ADOBECODEBANC", "ABC"))