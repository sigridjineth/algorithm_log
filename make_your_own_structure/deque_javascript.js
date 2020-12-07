// https://stackoverflow.com/questions/60052873/how-to-implement-deque-data-structure-in-javascript

class Deque {
  constructor() {
      this.front = this.back = undefined;
  }
  addFront(value) {
      if (!this.front) this.front = this.back = { value };
      else this.front = this.front.next = { value, prev: this.front };
  }
  removeFront() {
      let value = this.peekFront();
      if (this.front === this.back) this.front = this.back = undefined;
      else (this.front = this.front.prev).next = undefined;
      return value;
  }
  peekFront() { 
      return this.front && this.front.value;
  }
  addBack(value) {
      if (!this.front) this.front = this.back = { value };
      else this.back = this.back.prev = { value, next: this.back };
  }
  removeBack() {
      let value = this.peekBack();
      if (this.front === this.back) this.front = this.back = undefined;
      else (this.back = this.back.next).back = undefined;
      return value;
  }
  peekBack() { 
      return this.back && this.back.value;
  }
}

let deque = new Deque;
console.log(deque.peekFront()); // undefined
deque.addFront(1);
console.log(deque.peekBack()); // 1
deque.addFront(2);
console.log(deque.removeBack()); // 1
deque.addFront(3);
deque.addFront(4);
console.log(deque.peekBack()); // 2
deque.addBack(5);
deque.addBack(6);
console.log(deque.peekBack()); // 6
console.log(deque.removeFront()); // 4
console.log(deque.removeFront()); // 3
console.log(deque.removeFront()); // 2
console.log(deque.removeFront()); // 5
console.log(deque.removeFront()); // 6
console.log(deque.removeFront()); // undefined