import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # < go left
        # >= go right
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value) 
            else: 
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: self.right.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # To search a given key in Binary ¸¸¸¸¸¸¸¸¸compare it with root, if the key is present at root, we return root. If key is greater than root's key, we recur for right subtree of root¸¸¸¸¸¸¸¸¸r left subtree. 
        if self.value == target:
            return True
        
        if target < self.value:
            if not self.left:
                return False
            else: 
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        

    # Return the maximum value found in th¸¸¸¸¸¸¸¸¸
    def get_max(self):
        # go right until the end
        pass

    # Call the function `cb` on the value ¸¸¸¸¸¸¸¸¸
    # You may use a recursive or iterative¸¸¸¸¸¸¸¸¸
    def for_each(self, cb):
        # visit every node exactly one tim¸¸¸¸¸¸¸¸¸
        # go left until you can't anymore,¸¸¸¸¸¸¸¸¸
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
