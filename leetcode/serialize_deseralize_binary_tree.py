class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        queue = collections.deque([root])
        # initalize index 0 as # and only use from index 1
        result = ['#']
        # tree bfs serialization
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data):
        # exception
        if data == '# #': # front is # and end is # too
            return None
        
        nodes = data.split()
        root = TreeNode(nodes[1]) # starting from index 1
        queue = collections.deque([root]) # initalize queue with index 1
        index = 2
        # using fast runner strategy to check the child node result in advance
        while queue:
            node = queue.popleft()
            if (nodes[index] != '#'):
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            if (nodes[index] != '#'):
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))