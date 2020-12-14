// 리트코드 3번 Longest Substring without repeating characters
let lengthOfLongestSubstring = function(s) {
    let used = {};
    max_length = start = 0;
    let split = s.split("");
    for (const [index, char] of split.entries()) {
        if (Object.keys(used).includes(char) && start <= used[char]) {
            start = used[char] + 1;
        } else {
            max_length = Math.max(...[max_length, index - start + 1]);
        };
        used[char] = index;
    };
    return max_length;
};