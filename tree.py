# Node Object
class Node:
  def __init__(self, data):
    self.data = data
    self.source = None                             # Parent node.
    self.links = []                                # Linked child node.
  def __repr__(self):
    return self.data
  def add(self, node):
    self.links.append(node)

# Tree Object  
class Tree:
  def __init__(self, root):
    self.root = root
    self.nodes = [root]
  def add(self, node):
    self.root.add(node)                            # Adds node to root
  def get(self, coords):
    i = 0
    depth = len(coords)
    current_node = self.root
    while i != depth:                              # Recurs until at correct depth.
      current_node = current_node.links[coords[i]] # Adds node to links.

      i = i + 1
    return current_node
  def gadd(self, node, target_coords):
    target = self.get(target_coords)               # Gets requested node.
    target.add(node)                               # Directly adds to target node.
