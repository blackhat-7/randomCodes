class PriorityQueue {
  constructor(size) {
    this.container = [];
    this.maxsize = size;
  }

  parent(i) { return Math.floor((i-1)/2); }
  left(i) { return 2*i + 1; }
  right(i) { return 2*i + 2; }

  enqueue(element) {
    this.container.splice()
  }


}

class Element {
  constructor(data, priority) {
    this.data = data;
    this.priority = priority;
  }
}


pq = PriorityQueue();
pq.print();
