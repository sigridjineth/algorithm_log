// 유효한 애너그램 LEETCODE #242
let isAnagram_charCodeAt = function (s, t) {
  const ans = new Array(26).fill(0);

  for (let i = 0; i < s.length; i++) {
    ans[s.charCodeAt(i) - 97]++;
  }

  for (let i = 0; i < t.length; i++) {
    ans[t.charCodeAt(i) - 97]--;
  }

  for (let i = 0; i < 26; i++) {
    if (ans[i] !== 0) {
      return false;
    };
  }

  return true;
};

let isAnagram = (s, t) => {
    if (!s && !t) {
        return true;
    };
    if (!s || !t) {
        return false;
    };
    const sArr = [...s];
    const tArr = [...t];
    sArr.sort();
    tArr.sort();
    if (sArr.join('') === tArr.join('')) {
        return true;
    };
    return false;
};

let s = "anagram"
let t = "nagaram"
console.log(isAnagram(s, t));