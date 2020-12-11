// 중복 문자 제거 LEETCODE #316
// 재귀를 이용한 분리

let removeDuplicateLetters = function(s) {
    for (let char of [...(new Set(s.split("")))].sort()) {
        suffix = s.slice(s.indexOf(char));
        if (isSetsEqual(new Set(s.split("")), new Set(suffix))) {
            return char + removeDuplicateLetters(suffix.replace(new RegExp(char, "g"), ''));
        };
    };
    return '';
};

isSetsEqual = (a, b) => a.size === b.size && [...a].every(value => b.has(value));

const s = 'cbacdcbc';
console.log(removeDuplicateLetters(s));