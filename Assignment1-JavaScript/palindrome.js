
function LinkedList(val){
    this.val = val;
    this.next = null;
}

function isPalindrome(x) {
    if (!x || !Headers.next){
        return true; //if list has 0 or 1 element, return true as palindorme
    }
    let slow = x;
    let fast = x;
    //two pointer to move to middle of the list
    while (fast && fast.next){
        slow = slow.next;
        fast = fast.next.next;
    }
    //reversing list
    slow = reverse(slow);
    fast = x;

    while (slow){
        if (slow.val != fast.val){
            return false;
        }
        slow = slow.next;
        fast = fast.next;
    }
    return true;
}
    //reassign next pointer to previous node
function reverse(node){
    let prev = null;
    while (node){
        let nextNode = node.next;
        node.next = prev;
        prev = node;
        node = nextNode;
    }
    return prev;
}


console.log(isPalindrome("racecar"));  // true
console.log(isPalindrome("hello"));    // false
console.log(isPalindrome("i"));        // true
// r a c e c a r
//han nah => han han 

/* My solution 
function isPalindrome(x) {
    let string = String(x);

    if (string.length === 1) {
        return true;
    }

    let left = 0;
    let right = string.length - 1;

    while (left < right) {
        if (string[left] !== string[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
*/ 