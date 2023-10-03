# Define a class for the tree nodes
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Define the BinarySearchTree class
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Search for a key in the tree
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    # Insert a key into the tree
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node
    
    # Delete a key from the tree
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_key = self._find_min_key(node.right)
            node.key = min_key
            node.right = self._delete_recursive(node.right, min_key)
        
        return node
    
    def _find_min_key(self, node):
        while node.left:
            node = node.left
        return node.key
    
    # Print keys in ascending order
    def print_in_order(self):
        self._print_in_order_recursive(self.root)
    
    def _print_in_order_recursive(self, node):
        if node:
            self._print_in_order_recursive(node.left)
            print(node.key, end=' ')
            self._print_in_order_recursive(node.right)

# Example usage
bst = BinarySearchTree()
bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(3)

print("In-order traversal:")
bst.print_in_order()

print("\nSearching for key 3:", bst.search(3))
print("Searching for key 6:", bst.search(6))

print("Deleting key 2:")
bst.delete(2)
bst.print_in_order()
