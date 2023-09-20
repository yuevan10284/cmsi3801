class TreeNode {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
function isBalanced(root) {
    return checkHeight(root) !== -1;
}

function checkHeight(node){
    if (node == null){
        return 0;
    }
    const leftHeight = checkHeight(node.left);
    if (leftHeight === -1){
        return -1;
    }
    const rightHeight = checkHeight(node.right);
    if (rightHeight === -1){
        return -1;
    }
    const heightDiff = Math.abs(leftHeight - rightHeight);
    if (heightDiff > 1){
        return -1; 
    }
    else{
        return Math.max(leftHeight,rightHeight) + 1;
    }
}


const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);
root.left.left.left = new TreeNode(6);

console.log(isBalanced(root));  // false


const balancedRoot = new TreeNode(10);
balancedRoot.left = new TreeNode(6);
balancedRoot.right = new TreeNode(15);
balancedRoot.left.left = new TreeNode(4);
balancedRoot.left.right = new TreeNode(8);
balancedRoot.right.left = new TreeNode(12);
balancedRoot.right.right = new TreeNode(18);

console.log(isBalanced(balancedRoot));  // true


