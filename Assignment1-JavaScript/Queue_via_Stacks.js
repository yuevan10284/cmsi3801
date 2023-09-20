class Queue {
    constructor (){
        this.stack1 = []; //push
        this.stack2 = []; //pops
    }
    //enqueue 
    enqueue(element){
        this.stack1.push(element);
    }
    //dequeue
    dequeue(){
        if (this.stack2.length == 0){
            while (this.stack1.length > 0){
                this.stack2.push(this.stack1.pop());
            }
        }
        if (this.stack2.length === 0){
            throw new Error("Empty Queue");
        }
        return this.stack2.pop();
    }
    isEmpty() {
        return this.stack1.length === 0 &&this.stack2.length === 0;
    }

}
// Test
const q = new Queue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
console.log(q.dequeue());  // 1
console.log(q.dequeue());  // 2
q.enqueue(4);
console.log(q.dequeue());  // 3
console.log(q.dequeue());  // 4
