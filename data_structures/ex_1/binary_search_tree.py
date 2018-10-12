class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    arr = []
    arr.append(self)
    while len(arr) > 0:
      currentNode = arr.pop()
      if currentNode.right is not None:
        arr.append(currentNode.right)
      if currentNode.left is not None: 
        arr.append(currentNode.left)
      cb(currentNode.value)

  def breadth_first_for_each(self, cb):
    arr = []
    arr.append(self)
    while len(arr) > 0:
      currentNode = arr.pop(0)
      if currentNode.left is not None:
        arr.append(currentNode.left)
      if currentNode.right is not None:
        arr.append(currentNode.right)
      cb(currentNode.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
