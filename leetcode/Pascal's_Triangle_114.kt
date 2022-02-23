private fun getRow(rowIndex: Int): List<Int> {
    if (rowIndex == 0) {
        // return [1]
        return listOf(1)
    }
    return generateTriangle(1, rowIndex, listOf(1))
}

private fun generateTriangle(index: Int, rowIndex: Int, previous: List<Int>) : List<Int> {
    if (index > rowIndex) {
        return previous
    }
    
    val currentRow = MutableList(index + 1) { 1 }
    
    // 0 and lastIndex === 1
    for (i in 1..index) {
        currentRow[i] = (previous.getOrNull(i - 1) ?: 0) + (previous.getOrNull(i) ?: 0)
    }
    
    // rowIndex가 index 넘어가기 전까지. 넘어가면 if문 위에서 return previous!
    return generateTriangle(index + 1, rowIndex, currentRow)
}

fun main() {
    println(getRow(rowIndex = 3))
    println(getRow(rowIndex = 4))
}
