solutionForSiQ = () => {
    let nk = window.prompt().split(" ");
    let n = nk[0];
    let k = nk[1];
    let firstArray = window.prompt().split(" ");
    let secondArray = window.prompt().split(" ");
    
    // 첫 번째 배열을 정렬한다.
    for (let i = 0; i < firstArray.length; i++) {
        // 가장 작은 원소의 인덱스
        min_index = i;
        for (let j = 1; j < firstArray.length; j++) {
            if (firstArray[min_index] > firstArray[j]) {
                min_index = j;
            };
        };
        let temp = firstArray[i];
        firstArray[i] = firstArray[min_index];
        firstArray[min_index] = temp;
    }

    // 두 번째 배열을 정렬
    for (let i = 0; i < secondArray.length; i++) {
        // 가장 큰 원소의 인덱스
        max_index = i;
        for (let j = i + 1; j < secondArray.length; j++) {
            if (secondArray[max_index] < secondArray[j]) {
                max_index = j;
            };
        };
        let temp = secondArray[i];
        secondArray[i] = secondArray[max_index];
        secondArray[max_index] = temp;
    }

    for (let i = 0; i < k; k++) {
        if (firstArray[i] < secondArray[i]) {
            let tempA = firstArray[i];
            firstArray[i] = secondArray[i];
            secondArray[i] = tempA;
        } else {
            break;
        }
    }

    let sum = 0;
    firstArray.forEach((element) => {
        sum = sum + parseInt(element);
    });

    return sum;
}
