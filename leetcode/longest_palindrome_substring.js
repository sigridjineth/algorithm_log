// Longest Palindrome Substring Leetcode 5

solution = (str) => {
    function expand(str, left, right) {
        while (left >= 0 && right < str.length && str[left] === str[right]) {
            left--, right++;
        }
        return str.substring(left+1, right);
    }

    function getLongestStrings(arrayOfStrings) {
        let maxLng = Math.max(...applyOfStrings.map(element => element.length));
        return arrayOfStrings.filter(element => element.length === maxLng)[0] // array 형태로 반환되므로 주의
    }

    if (str.length < 2) {
        return str;
    }

    let result = "";
    for (let i = 0; i < str.length - 1; i++) {
        temp = [result, expand(str, i, i), expand(str, i, i + 1)];
        result = getLongestStrings(temp)
    }

    return result;
}