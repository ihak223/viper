from viper.tree import *
from viper.builtins.ciphers import CeasarShift

root = Node("root")
tree = Tree(root, debug=True)
tree.add(Node("test"))
tree.gadd(Node("test2"), [0])
tree.gadd(Node("test3"), [0])
tree.gadd(Node("test4"), [0, 1])
print(tree.get([0, 0]))
print(tree.get([0, 1]))

test = CeasarShift()
print(test.decrypt(3, "XIWX"))




