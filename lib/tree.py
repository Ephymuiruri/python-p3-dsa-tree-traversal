class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit=[self.root]
    while nodes_to_visit:
      node=nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      if'children' in node:
        nodes_to_visit = node['children']+ nodes_to_visit
    return None

