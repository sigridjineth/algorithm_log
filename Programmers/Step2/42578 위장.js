function solution(clothes) {
    var closet = clothes.reduce(function(acc, cur) {
        acc[cur[1]] = acc[cur[1]] ? acc[cur[1]] + 1 : 1
        return acc;
    }, {})

    var item = Object.values(closet);
    if (item.length == 1) {
        return item[0];
    } else {
        var result = 1
        item.forEach(function(x) {
            return result *= (x + 1);
        });
    };
    return result - 1
};