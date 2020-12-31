let characterReplacement = function(s, k) {
    function counter(object) {
        let keys = Object.keys(object)
        let result = -1
        keys.forEach((key) => result = Math.max(...[result, object[key]]))
        return result
    }
    let left = 0
    let counts = {}
    let right_r = 0
    for (let right = 1; right < s.length + 1; right++) {
        if (!counts[s[right-1]]) {
            counts[s[right-1]] = 1
        } else {
            counts[s[right-1]] += 1
        }
        let max_char_n = counter(counts)
        if (right - left - max_char_n > k) {
            counts[s[left]] -= 1
            left += 1
        }
        right_r = right
    }
    return right_r - left
};