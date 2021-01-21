function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
};

let serialize = function(root) {
    if (root != null && root.val === undefined) {
        return "#";
    };
    let result = ['#']
    let queue = [root];
    while (queue.length > 0) {
        let node = queue.shift();
        if (node !== null) {
            queue.push(node.left);
            queue.push(node.right);
            result.push(node.val.toString());
        } else {
            result.push('#');
        };
    };
    return result.toString();
};

let deserialize = function(temp) {
    if (temp === '# #') {
        return [];
    };
    if (temp === '#') {
        return [];
    };
    let data = temp.replace(/,/g, "");
    let nodes = data.split("");
    let root = new TreeNode(Number.parseInt(nodes[1]));
    let queue = [root];
    let index = 2;
    while (queue.length > 0) {
        let node = queue.shift();
        if (nodes[index] !== '#') {
            node.left = new TreeNode(Number.parseInt(nodes[index]));
            queue.push(node.left);
        };
        index += 1;
        if (nodes[index] !== '#') {
            node.right = new TreeNode(Number.parseInt(nodes[index]));
            queue.push(node.right);
        };
        index += 1;
    };
    return root;
};

let one = new TreeNode(1);
let two = new TreeNode(2);
let three = new TreeNode(3);
let nothing = new TreeNode(null);
let four = new TreeNode(4);
let five = new TreeNode(5);
one.left = two
one.right = three
three.left = four
three.right = five
console.log(serialize(deserialize(serialize(one))));

let nothing_two = new TreeNode();
console.log(serialize(deserialize(serialize(nothing_two))));