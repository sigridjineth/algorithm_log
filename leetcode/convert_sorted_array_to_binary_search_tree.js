// 정렬된 배열의 이진 탐색 트리 변환
// LEETCODE #108
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
};
let sortedArrayToBST = function(nums) {
    if (nums.length === 0 || nums === undefined) {
        return null;
    };
    let mid = Math.floor(nums.length / 2);
    // divide and conquery to convert the BST
    let node = new TreeNode(nums[mid]);
    node.left = sortedArrayToBST(nums.slice(0, mid));
    node.right = sortedArrayToBST(nums.slice(mid+1, nums.length));
    return node;
};