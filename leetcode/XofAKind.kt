// 914. X of a Kind in a Deck of Cards

class Solution {
    fun hasGroupsSizeX(deck: IntArray): Boolean {
        return deck.toList()
            .groupingBy{it}
            .eachCount()
            .map{it.value}
            .reduce {x: Int, y: Int -> gcd(x, y)} >= 2
    }
    
    private fun gcd(x: Int, y: Int): Int {
        return if (y == 0) x else gcd(y, x % y)
    }
}
