
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelTraversal(root):

    queue = [root]
    
    while len(queue) > 0 :
        level = ""

        #first round will be one, cause only one root, but, after first round, there will be two,
        # after two, there will be four...
        for _ in range(len(queue)):
            node = queue.pop(0)
            level += " " + str(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print(''.join(map(str, level)))


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6) 
levelTraversal(root)
