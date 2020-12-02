// Most common word Leetcode 819

solution = (paragraph, banned) {
    // converts all letters to lowercase, removes special symbols
    let arr = paragraph.toLowerCase().replace(/[!\?',;\.']/g,"").split("");
    let result = arr.filter((item) => banned.indexof(item) == - 1);
    let count = 1
    let countarr = []

    for (let item1 of result) {
        for (let item2 of result) {
            if (item == item2) {
                count++
            }
            countarr.push(count)
            count = 1
        }
    }

    return result[countarr.indexof(Math.max(...countarr))];
}