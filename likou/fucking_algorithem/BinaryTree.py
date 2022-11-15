"""
二叉树相关的问题
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
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

if __name__ == "__main__":
    s = Solution
    root = [1,None,2,3]
    print(s.inorderTraversal(root))
    
