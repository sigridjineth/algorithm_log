class MinHeap {
    constructor() {
        this.heap = [null]
    }
    getMin(){
        return this.heap[1]
    }
    insert(node) {
        this.heap.push(node)
        if (this.heap.length > 1) {
            let current = this.heap.length - 1
            while (current > 1 && this.heap[Math.floor(current/2)].dist > this.heap[current].dist) {
                [this.heap[Math.floor(current/2)], this.heap[current]] = [this.heap[current], this.heap[Math.floor(current/2)]]
                current = Math.floor(current/2)
            }
        }
    }
    remove() {
        /* Smallest element is at the index 1 in the heap array */
        let smallest = this.heap[1]

        /* When there are more than two elements in the array, we put the right most element at the first position
            and start comparing nodes with the child nodes
        */
        if (this.heap.length > 2) {
            this.heap[1] = this.heap[this.heap.length-1]
            this.heap.splice(this.heap.length - 1)

            if (this.heap.length === 3) {
                if (this.heap[1].dist > this.heap[2].dist) {
                    [this.heap[1], this.heap[2]] = [this.heap[2], this.heap[1]]
                }
                return smallest
            }

            let current = 1
            let leftChildIndex = current * 2
            let rightChildIndex = current * 2 + 1

            while (this.heap[leftChildIndex] &&
                    this.heap[rightChildIndex] &&
                    (this.heap[current].dist > this.heap[leftChildIndex].dist ||
                        this.heap[current].dist > this.heap[rightChildIndex].dist)) {
                if (this.heap[leftChildIndex].dist < this.heap[rightChildIndex].dist) {
                    [this.heap[current], this.heap[leftChildIndex]] = [this.heap[leftChildIndex], this.heap[current]]
                    current = leftChildIndex
                } else {
                    [this.heap[current], this.heap[rightChildIndex]] = [this.heap[rightChildIndex], this.heap[current]]
                    current = rightChildIndex
                }

                leftChildIndex = current * 2
                rightChildIndex = current * 2 + 1
            }
        }

        /* If there are only two elements in the array, we directly splice out the first element */

        else if (this.heap.length === 2) {
            this.heap.splice(1, 1)
        } else {
            return null
        }

        return smallest
    }
}

kClosest = (points, K) => {
    let heap = new MinHeap()
    for (let element of points) {
        let x = element[0]
        let y = element[1]
        let dist = x ** 2 + y ** 2
        heap.insert({dist: dist, x: x, y: y})
    }
    let result = []
    for (let i = 0; i < K; i++){
        let element = heap.remove()
        result.push([element.x, element.y])
    }
    return result
}

let points = [[1,3], [-2,2]]
let K = 1
console.log(kClosest(points, K))