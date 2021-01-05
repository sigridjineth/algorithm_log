// LEETCODE 455
// 그리디 알고리즘
findContentChildren = (g, s) => {
    g.sort(function (a, b) {
        return a - b
    })
    s.sort(function (a, b) {
        return a - b
    })
    let child_i = 0
    let cookie_j = 0
    // 만족하지 못할 때까지 그리디 진행
    while (child_i < g.length && cookie_j < s.length) {
        // 만약 cookie가 greedy함을 넘으면
        if (s[cookie_j] >= g[child_i]) {
            // 1명을 추가한다.
            child_i += 1
        }
        // 그 다음에는 무조건 그 다음 쿠키를 탐색한다.
        cookie_j += 1
    }
    return child_i
}

// 아래는 통과하지 않는다. 이유는 잘 모르겠다. bisect_right을 똑같이 구현하면 될 것 같은데 말이다. :(
findContentChildren_binarySearch = (g, s) => {
    function bisect_right(nums, left, right, target) {
        if (left <= right) {
            let mid = Math.floor((left + right) / 2)
            if (nums[mid] < target) {
                return bisect_right(nums, mid + 1, right, target)
            } else if (nums[mid] > target) {
                return bisect_right(nums, left, mid - 1, target)
            } else {
                return mid
            }
        } else {
            return -1
        }
    }
    g.sort(function(a, b) {
        return a - b
    })
    s.sort(function(a, b) {
        return a - b
    })
    let result = 0
    for (let i of s) {
        // 이진 검색으로 더 큰 인덱스를 탐색한다.
        // 하나의 리스트를 순회하면서 다른 하나는 이진 검색으로 찾는다.
        let index = bisect_right(g, 0, g.length-1, i) + 1
        if (index > result) {
            result += 1
        }
    }
    return result
}

findContentChildren_reduce = (g, s) => {
    const asc = (a, b) => a - b;
    g.sort(asc);
    return s.sort(asc).reduce((a, size) => size >= g[a] ? ++a: a, 0)
}

let g = [1,2]
let s = [1,2,3]
console.log(findContentChildren_binarySearch(g, s))