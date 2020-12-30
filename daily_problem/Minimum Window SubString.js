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