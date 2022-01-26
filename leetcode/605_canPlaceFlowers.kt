class Solution {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        return n <= listOf(1, 0, *flowerbed.toTypedArray(), 0, 1)
                .asSequence()
                .mapIndexed { index, value -> Pair(index, value) }
                .filter { it.second == 1 }
                .zipWithNext { a, b -> capability(b.first - a.first - 3) }
                .sum()
    }

 private fun capability(zeros: Int): Int {
     if (zeros < 0) {
         return 0
     } else {
 		return Math.ceil(zeros.toDouble() / 2).toInt()
     }
 }
}
