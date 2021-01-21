// Reverse String. Leetcode 344
// Two-pointer using swap. 범위를 줄여가며 포인트 2개를 이용해 풀이한다.

solution = (input) => {
    str = input.split("")
    left = 0
    right = str.length - 1

    while (left < right) {
        temp = str[left]
        str[left] = str[right]
        str[right] = temp
        left += 1
        right -= 1
    }

    return str
}