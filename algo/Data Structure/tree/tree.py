class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.queue = []

    def insert(self, data):
        # 如果下一個節點不是一個node
        if not self.data:
            self.data = data
            return
        # 如果有相同數值在node裡面
        if self.data == data:
            return
        # 如果該資料小於目前節點，往左邊建立樹節點
        if data < self.data:
            if self.left:  # 如果左節點不為None
                # 往下插入遞迴
                self.left.insert(data)
                return
            # 建立新結點
            self.left = Tree(data)
            return
        elif data > self.data:
            if self.right:
                self.right.insert(data)
                return
            self.right = Tree(data)

    def inorder(self, tree):
        if not tree:
            return
        self.inorder(tree.left)
        print(tree.data, end=" ")
        self.inorder(tree.right)

    def postorder(self, tree):
        if not tree:
            return
        self.postorder(tree.left)
        self.postorder(tree.right)
        print(tree.data, end=" ")

    def preorder(self, tree):
        if not tree:
            return
        print(tree.data, end=" ")
        self.preorder(tree.left)
        self.preorder(tree.right)

    def BFS(self):
        if self.data is None:
            return

        queue = [self]
        while queue:
            current = queue.pop(0)
            print(current.data, end=' ')

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def search(self, target):
        if self is None or self.data == target:
            return self
        if target < self.data:
            return self.search(self.left)
        else:
            return self.search(self.right)


def search_while(tree, target):
    while tree is not None and tree.data != target:
        if tree.data > target:
            tree = tree.left
        else:
            tree = tree.right
    if tree is None:
        print("No such value")
    else:
        print(tree.data)
    return tree


root = Tree()
root.insert(15)
root.insert(6)
root.insert(5)
root.insert(1)
root.insert(13)
root.insert(-7)
root.insert(3)
print("Preorder Traversal", end=" ")
root.preorder(root)
print("\nInorder Traversal", end=" ")
root.inorder(root)
print("\nPostorder Traversal", end=" ")
root.postorder(root)
print("\nBFS Traversal", end=" ")
root.BFS()
print()
search_while(root, 13)

