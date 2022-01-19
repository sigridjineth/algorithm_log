class Solution {
    private inline fun IntArray.isPlateau(i: Int) = (get(i) == get(i + 1))
    private inline fun IntArray.isValley(i: Int) = (i > 0 && get(i - 1) > get(i) && get(i) < get(i + 1))
    private inline fun IntArray.isPeak(i: Int) = (i > 0 && get(i - 1) < get(i) && get(i) > get(i + 1))

    fun validMountainArray(arr: IntArray): Boolean {
        var hasPeak = false
        repeat(arr.size - 1) { i ->
            if (arr.isPlateau(i) || arr.isValley(i)) {
                return false
            }
            if (!hasPeak) {
                hasPeak = arr.isPeak(i)
            }
        }
        return hasPeak
    }
}
