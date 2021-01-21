// LEETCODE 369 Intersection of Two Arrays
intersection_bruteForce = (nums1, nums2) => {
    let result = new Set()
    for (let element of nums1) {
        for (let element2 of nums2) {
            if (element === element2) {
                result.add(element)
            }
        }
    }
    return result
}

intersection_twoPointers = (nums1, nums2) => {
    let result = new Set()
    nums1.sort()
    nums2.sort()
    let i = 0
    let j = 0
    // 투 포인터 우측으로 이동하여 일치 여부 판별
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] > nums2[j]) {
            j += 1
        } else if (nums1[i] < nums2[j]) {
            i += 1
        } else {
            result.add(nums1[i])
            i += 1
            j += 1
        }
    }
    return result
}

intersection_binarySearch = (nums1, nums2) => {
    function binarySearch(nums, left, right, target) {
        if (left <= right) {
            let mid = Math.floor((left + right) / 2)
            if (nums[mid] < target) {
                return binarySearch(mid + 1, right)
            } else if (nums[mid] > target) {
                return binarySearch(left, mid - 1)
            } else {
                return mid
            }
        } else {
            return -1
        }
    }
    let result = new Set()
    nums2.sort()
    for (let n1 of nums1) {
        let l2 = binarySearch(nums2, 0, nums2.length - 1, n1)
        if (nums2.length > 0 && nums2.length > l2 && n1 === nums2[l2]) {
            result.add(n1)
        }
    }
    return result
}