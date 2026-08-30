# 297. Serialize and Deserialize Binary Tree
# Problem: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Submitted: 2026-08-30 14:38 EDT
# Intuition: Preorder values plus null markers preserve both tree values and structure.
# Approach: Serialize with recursive preorder and deserialize by consuming tokens in the same order.
# Complexity: O(n) time and space under bounded node values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def recurseSerialize(self, root):
        if root is None:
            self.serialized.append("None")
            return
        
        self.serialized.append(str(root.val))
            
        self.recurseSerialize(root.left)
        self.recurseSerialize(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        self.serialized= []
        self.recurseSerialize(root)
        return ",".join(self.serialized)


    def recurseDeserialize(self,) -> Optional([TreeNode]):

        val = self.data[self.i]
        self.i += 1

        if val == "None":
            return None
        
        head = TreeNode(int(val))

        head.left = self.recurseDeserialize()
        head.right = self.recurseDeserialize()

        return head
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        self.data = data.split(",")
        self.i = 0

        return self.recurseDeserialize()




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))