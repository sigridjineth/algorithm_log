// 자바스크립트로 구현하는 Deque 자료구조
// https://velog.io/@jakeseo_me/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%A1%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0-3-Deque-%EA%B5%AC%ED%98%84-%EB%B0%8F-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4

class Deque {
  constructor() {
    this.data = [];
    this.rear = 0;
  }

  push_front(element) {
    this.data.unshift(element);
    this.rear = this.rear + 1;
  }

  push_back(element) {
    this.data[this.rear] = element;
    this.rear = this.rear + 1;
  }

  pop_front() {
    if (this.isEmpty() === false) {
      this.rear = this.rear - 1;
      return this.data.shift();
    }

    return false;
  }

  pop_back() {
    if (this.isEmpty() === false) {
      this.rear = this.rear - 1;
      return this.data.pop();
    }

    return false;
  }

  length() {
    return this.rear;
  }

  isEmpty() {
    return this.rear === 0;
  }

  getFront() {
    if (this.isEmpty() === false) {
      return this.data[0];
    }

    return false;
  }

  getLast() {
    if (this.isEmpty() === false) {
      return this.data[this.rear - 1];
    }

    return false;
  }

  print() {
    for (let i = 0; i < this.rear; i++) {
      console.log(this.data[i]);
    }
  }
}