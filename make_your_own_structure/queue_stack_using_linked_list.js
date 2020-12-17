// Implementing Stack using linked list
class Stack {
    constructor() {
      this.top = null;
    }
    makeNode(value) {
      return {
        value,
        below: null,
      };
    }
    push(...values) {
      for (let value of values) {
        const node = this.makeNode(value);
        if (this.top === null) {
          this.top = node;
        } else {
          node.below = this.top;
          this.top = node;
        }
      }
    }
    pop() {
      if (this.size() === 0) return;
      let popped;
      if (this.top && this.top.below) {
        popped = this.top;
        this.top = this.top.below;
      } else {
        popped = this.top;
        this.top = null;
      }
      return popped.value;
    }
    contains(value) {
      let clone = this.top;
      while (clone !== null) {
        if (clone.value === value) {
          return true;   
        }
        clone = clone.below;
      }
      return false;
    }
    size() {
      let count = 0;
      let clone = this.top;
      while (clone !== null) {
        count += 1;
        clone = clone.below;
      }
      return count;
    }
  };

  // Implementing Queue using two stacks
  class Queue {
    constructor() {
      this.inbox = new Stack();
      this.outbox = new Stack();
    }
    enqueue(value) {
      this.inbox.push(value);
    }
    dequeue() {
      const size = this.inbox.size();
      let temp_size = size;
      while (temp_size > 0) {
        this.outbox.push(this.inbox.pop());
        temp_size -= 1;
      }
      const dequeued = this.outbox.pop();
      temp_size = size - 1;
      while (temp_size > 0) {
        this.inbox.push(this.outbox.pop());
        temp_size -= 1;
      }
      return dequeued;
    }
    contains(value) {
      return this.inbox.contains(value);
    }
    size() {
      return this.inbox.size();
    }
  };