// Realignment of Log files Leetcode 937

solution = (logs) => {
    letters = []
    numbers = []

    for (let log of logs) {
        element = log.split(" ")
        if (element[0].includes("dig")) {
            numbers.push(log)
        } else {
            letters.push(log)
        }
    }

    letters.sort(function(a, b) {
        return a[0] - b[0] ? -1 : 1
    })

    return letters + numbers
}