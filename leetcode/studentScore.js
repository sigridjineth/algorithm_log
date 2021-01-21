selectionSort = (array) => {
    for (let i = 1; i < array.length; i++) {
        for (let j = i; j > 0; j--) {
            if (array[j].score < array[j-1].score) {
                let tempSmallData = array[j];
                let tempBigData = array[j-1];
                array[j] = tempBigData;
                array[j-1] = tempSmallData;
            } else {
                break;
            }
        }
    }
}

getMap = () => {
    let n = window.prompt();
    array = [];
    for (let index = 0; index < n; index++) {
        array.push(window.prompt().split().map((element) => {
            return parseInt(element);
        }))
    }
    return array;
}

solutionForThreeQ = () => {
    let array = getMap();
    selectionSort(array);
    return array;
}
