// LEETCODE 240 Search a 2D Matrix II
searchMatrix = (matrix, target) => {
    if (!matrix) {
        return false
    }
    let row = 0
    let col = matrix[0].length - 1
    let tot = matrix.length - 1
    while (row <= tot && col >= 0) {
        if (target === matrix[row][col]) {
            return true
        } else if (target < matrix[row][col]) {
            col -= 1 // 한 칸 왼쪽으로 옮긴다.
        } else if (target > matrix[row][col]) {
            row += 1 // 아래 행으로 이동한다.
        } else {
            return false
        }
    }
    return false
}