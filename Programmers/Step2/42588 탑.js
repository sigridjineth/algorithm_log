function solution(heights) {
    var answer = [];
    while (heights.length != 0) {
        rights = heights.pop()
        receive = 0
        heights.map = function(compare) {
            if (compare > rights) {
                receive += 1
            }
            answer.pop(receive)
        }
        return answer;
    }
};

heights = [6, 9, 5, 7, 4]
solution(heights)