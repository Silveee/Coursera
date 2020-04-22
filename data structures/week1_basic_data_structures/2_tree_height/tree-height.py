# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parents = [int(x) for x in sys.stdin.readline().split()]
                self.tree = [[] for x in self.parents]
                for index, parent in enumerate(self.parents):
                        if parent == -1:
                                self.root_index = index
                        else:
                                self.tree[parent].append(index)

        def compute_height(self, root=None):
                if root is None:
                        root = self.root_index
                if root == -1:
                        return 0

                if not len(self.tree[root]):
                        return 1
                height = 1 + max([self.compute_height(node) for node in self.tree[root]])
                return height


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
