def solution(rows, columns, queries):
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    num = 1
    for row in range(rows):
        for column in range(columns):
            array[row][column] = num
            num = num + 1
    for (x1, y1, x2, y2) in queries:
        temp = array[x1 - 1][y1 - 1]
        ans = temp
        for k in range(x1 - 1, x2 - 1):
            element = array[k + 1][y1 - 1]
            array[k][y1 - 1] = element
            ans = min(ans, element)
        for k in range(y1 - 1, y2 - 1):
            element = array[x2 - 1][k + 1]
            array[x2 - 1][k] = element
            ans = min(ans, element)
        for k in range(x2 - 1, x1 - 1, -1):
            element = array[k - 1][y2 - 1]
            array[k][y2 - 1] = element
            ans = min(ans, element)
        for k in range(y2 - 1, y1 - 1, -1):
            element = array[x1 - 1][k - 1]
            array[x1 - 1][k] = element
            ans = min(ans, element)
        array[x1 - 1][y1] = temp
        answer.append(ans)
    return answer
