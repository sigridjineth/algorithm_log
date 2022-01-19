class Solution {
    fun isLongPressedName(name: String, typed: String): Boolean {
        var p1 = 0
        var p2 = 0
        var prevCh1: Char? = null
        
        while (p1 < name.length || p2 < typed.length) {
            val ch1 = name.getOrNull(p1)
            val ch2 = typed.getOrNull(p2)
            // if ch1 ch2 the same
            if (ch1 == ch2) {
                p1 += 1
                p2 += 1
                prevCh1 = ch1
                continue
            } else if (prevCh1 == ch2) {
                p2 += 1
                continue
            } else {
                return false
            }
        }
        return true
    }
}
