function solution(participant, completion) {
    var dic = completion.reduce(function(obj, t) {
        (obj[t] = obj[t] ? obj[t] + 1 : 1);
        return obj;
    }, {});
    return participant.find(function(player) {
        if (dic[player] == true) {
            dic[player] = dic[player] - 1;
        } else {
            return true;
        };
    });
};
//실행은 통과되는데 다른 테스트 케이스에 통과되지 못함. 그 이유가 뭔지 도대체 궁금함