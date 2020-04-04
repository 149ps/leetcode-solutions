"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        global res
        res = ''
        if not root:
            return 'None,'
        res += str(root.val) + ','
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def recDeserialize(node_list):
            if node_list[0] == 'None':
                node_list.pop(0)
                return None
            root = TreeNode(node_list[0])
            node_list.pop(0)
            root.left = recDeserialize(node_list)
            root.right = recDeserialize(node_list)
            return root
        data_list = data.split(',')
        return recDeserialize(data_list)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))