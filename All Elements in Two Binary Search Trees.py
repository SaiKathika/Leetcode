class Solution:
    def getAllElements(root1, root2):
        lst1, lst2 = [], []

        def inordertraverse(root, lst):
            if not root: return
            inordertraverse(root.left, lst)
            lst.append(root.val)
            inordertraverse(root.right, lst)

        inordertraverse(root1, lst1)
        inordertraverse(root2, lst2)

        finallst = sorted(lst1 + lst2)

        return finallst