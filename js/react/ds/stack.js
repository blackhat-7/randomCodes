class Stack {
    constructor() {
        this.items = [];
    }

    push(data) {
        this.items.push(data);
    }

    pop() {
        if (this.isEmpty())
            return false;
        return this.items.pop();
    }

    size() {
        return this.items.length;
    }

    isEmpty() {
        return this.items.length == 0;
    }

    print() {
        this.items.forEach(item => process.stdout.write(item + " "));
        console.log();
    }
}

let stack = new Stack()
stack.push(0);
stack.push(6);
stack.push(7);
stack.push(3);
stack.print()
stack.pop();
stack.push(2);
stack.print();
