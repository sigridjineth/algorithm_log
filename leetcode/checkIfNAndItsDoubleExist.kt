// 1346. Check If N and Its Double Exist

class Solution {
    fun checkIfExist(arr: IntArray): Boolean {
    val s = hashSetOf<Int>()
    return arr.fold(false, { a, b -> when {
        s.contains(b * 2) || b % 2 == 0 && s.contains(b / 2) -> true
        else -> {s.add(b); a } }
        })
    }
}
