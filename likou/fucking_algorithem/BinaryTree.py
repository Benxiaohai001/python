"""
二叉树相关的问题
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode1:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    """
    LeeCode 94:给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
    输入：root = [1,null,2,3]
    输出：[1,3,2]
    没办法在本地运行；缺少数据结构
    """
    def zhongxu(self, root, arr):
        if root is None:
            return
        self.zhongxu(root.left, arr)
        arr.append(root.val)
        self.zhongxu(root.right, arr)


    def inorderTraversal(self, root):
        arr = []
        self.zhongxu(root,arr)
        return arr


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, treenode) -> None:
        self._head = treenode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]):
        cur = root
        stack = []
        arr = []
        while cur or stack:
            while cur:
                arr.append(cur.val)
                # cur = cur.right
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            cur = stack.pop()
            arr.append(cur.val)
            cur = cur.left
            
            
            
        return arr




if __name__ == "__main__":
    s = Solution
    root2 = TreeNode(2, 3, None)
    root1 = TreeNode(1, None, root2)
    root = BinaryTree(root1)
    print(s.preorderTraversal(root))
    
