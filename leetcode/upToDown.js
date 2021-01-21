sort = (array, start, end) => {
    // 원소가 한 개 일 때는 종료한다.
    if (start >= end) {
        return;
    }
    // 피벗은 첫 번째 원소이다 
    let pivot = start;
    let left = start + 1;
    let right = end;
    // 1단계를 수행한다.
    while (left <= right) {
        // 피벗보다 큰 데이터를 찾을 때까지 반복한다.
        while ((left <= end) && array[left] < array[pivot]) {
            left = left + 1;
        }
        // 피벗보다 작은 데이터를 찾을 때까지 반복한다.
        while ((right >= start) && (array[right] >= array[pivot])) {
            right = right + 1;
        }
        // 만약 엇갈렸다면 작은 데이터와 피벗을 서로 교체한다.
        if (left > right) {
            let tempSmallData = array[right];
            let tempPivot = array[pivot];
            array[right] = tempPivot;
            array[pivot] = tempSmallData;
        } else {
            let tempBigData = array[left];
            let tempSmallData = array[right];
            array[right] = tempBigData;
            array[left] = tempSmallData;
        };
        sort(array, start, right - 1);
        sort(array, right + 1, end);
    };
};

getMap = () => {
    let n = window.prompt();
    array = [];
    for (let index = 0; index < n; index++) {
        array.push(window.prompt().split().map((element) => {
            return parseInt(element)
        }));
    }
    return array;
};

solution = () => {
    let array = getMap();
    sort(array, 0, array.length - 1);
    for (let i = array.length - 1; i >= 0; i--) {
        console.log(array[i], " ");
    };
};
