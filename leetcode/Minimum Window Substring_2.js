// Minimum Window Substring
function counter(string) {
    let array = string.split("")
    let count = {}
    array.forEach((val) => count[val] = (count[val] || 0) + 1);
    return count;
}

minWindow = (s, t) => {
    let need = counter(t)
    let missing = t.length
    let left = 0
    let start = 0
    let end = 0

    for (let element of s.split("").entries()) {
        let right = element[0] + 1
        let char = element[1]
        missing -= (need[char] > 0)
        need[char] = ((need[char] || 0) - 1)

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

let S = "ADOBECODEBANC"
let t = "ABC"
console.log(minWindow(S, t))