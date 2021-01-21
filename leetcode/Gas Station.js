// LEETCODE 134
// 모두 방문하는 기본적인 O(n^2) 풀이
canCompleteCircuit_basic = (gas, cost) => {
    for (let start = 0; start < gas.length; start++) {
        let fuel = 0
        for (let i = start; i < gas.length + start; i++) {
            let index = i % gas.length
            let can_travel = true
            if (gas[index] + fuel < cost[index]) {
                can_travel = false
                break
            } else {
                fuel += gas[index] - cost[index]
            }
        }
        if (can_travel) {
            return start
        }
        return -1
    }
}

// 귀류법을 이용하여 O(n)으로 풀이 최적화가 가능하다.
canCompleteCircuit = (gas, cost) => {
    // 전체 기름의 양이 전체 비용보다 클 경우 반드시 전체를 방문할 수 있는 출발점이 존재한다.
    if (gas.reduce((a, b) => { return a + b }, 0) < cost.reduce((a, b) => { return a + b }, 0)) {
        return -1
    }
    let start = 0
    let fuel = 0
    for (let i = 0; i < gas.length; i++) {
        // 비용이 더 클 때 리턴하면, 이제 반드시 존재하는 경우만 남아있게 된다.
        // 이 문제는 한 번 이상은 반드시 성립하지 않는 지점이 존재한다.
        // 출발점이 안 되는 지점을 판별해본다.
        if (gas[i] + fuel < cost[i]) {
            start = i + 1
            fuel = 0
        } else {
            fuel += gas[i] - cost[i]
        }
    }
    return start
}