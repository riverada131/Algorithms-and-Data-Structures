class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self is None:
            self = BST(value)
        elif value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                BST.insert(self.left, value)
        elif value > self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                BST.insert(self.right, value)
        return self


    def remove(value):
        pass

    def contains(self, value):
        if value == self.value:
            return True
        else:
            if value < self.value and self.left is not None:
                return BST.contains(self.left, value)
            elif value > self.value and self.right is not None:
                return BST.contains(self.right, value)
            else:
                return False
    
    def inOrderTraversal(self, results = []):
        if self is not None:
            BST.inOrderTraversal(self.left, results)
            results.append(self.value)
            BST.inOrderTraversal(self.right, results)
        return results
    
    def preOrderTraversal(self, results = []):
        if self is not None:
            results.append(self.value)
            BST.preOrderTraversal(self.left, results)
            BST.preOrderTraversal(self.right, results)
        return results
    
    def postOrderTraversal(self, results = []):
        if self is not None:
            BST.postOrderTraversal(self.left, results)
            BST.postOrderTraversal(self.right, results)
            results.append(self.value)
        return results
        
testArray = [10, 20, 32, 45, 6, 25, 3]
index = 0
for i in testArray:
    if index == 0:
        testTree = BST(i)
        index += 1
    else:
        BST.insert(testTree, i)
        index += 1
print(BST.contains(testTree, 32))
print(BST.contains(testTree, 4))
print(BST.inOrderTraversal(testTree))
print(BST.preOrderTraversal(testTree))
print(BST.postOrderTraversal(testTree))