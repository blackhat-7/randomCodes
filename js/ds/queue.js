class Queue {
    constructor() {
        this.items = [];
    }

    enqueue(item) {
        this.items.push(item);
    }

    dequeue() {
        if (this.isEmpty())
            return false;
        return this.items.shift()
    }
    
    isEmpty() {
        return this.items.length == 0;
    }

    print() {
        this.items.forEach(item => process.stdout.write(item + " "));
        console.log();
    }
}

let q = new Queue()
q.enqueue(6);
q.enqueue(4);
q.enqueue('random');
q.print();
q.dequeue()
q.enqueue(3);
q.enqueue(7);
q.print();
