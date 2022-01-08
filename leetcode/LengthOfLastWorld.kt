// 58. Length of Last Word

class Solution {
    fun lengthOfLastWord(s: String): Int {
        return s.reversed()
                .dropWhile{ it == ' '}
                .fold(0) { s, c -> if (c == ' ' ) return s else s+1
        }
    }
}
