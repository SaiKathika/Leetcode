#refer
#https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/836224/Python-Solution-or-Explanation-or-O(n)-or-4-lines-only

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.calcSum(root, 0)
    
    def calcSum(self, root, n):
        
        if(root == None): return 0
        
        n = n << 1 | root.val      #left shift a binary number
        
        if(root.left == None and root.right == None): return n
        return ( self.calcSum(root.left,n) + self.calcSum(root.right,n) )