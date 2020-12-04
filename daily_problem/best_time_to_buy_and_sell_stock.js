// Best Time to buy and sell stock LEETCODE #121

solution = (prices) => {
    let profit = 0;
    let min_price = Number.MAX_SAFE_INTEGER;

    // 최솟값과 최댓값을 계속 갱신
    for (let price of prices) {
        min_price = Math.min(...[min_price, price]);
        profit = Math.max(...[profit, price - min_price]);
    }

    return profit;
}

prices = [7,1,5,3,6,4];
console.log(solution(prices));