from viper.tree import *

root = Node("root")
tree = Tree(root)
tree.add(Node("test"))
tree.gadd(Node("test2"), [0])
print(tree.get([0, 0]))



