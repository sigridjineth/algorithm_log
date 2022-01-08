// 1805. Number of Different Integers in a String

class Solution {
    fun numDifferentIntegers(word: String): Int {
        return word.split("\\D+".toRegex())
                .filter{it.isNotBlank()}
                .map{it.replaceFirst("^0+".toRegex(), "")}
                .toSet()
                .size
    }
}
