class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:  # Binary tree Class
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if ch == 'L':
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i

    def traverseInorder(self, root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data, end=" ")
            self.traverseInorder(root.right)


def minDepth(root):
    pass


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = []
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k = 0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k += 3
        # tree.traverseInorder(root)
        # print ''
        # print(minDepth(root))
        print(lis[0])

