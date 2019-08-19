def deep_pre(node):
    """pre order scan two branch tree"""
    print(node.data)
    if node.left.data:
        deep_pre(node.left)
    if node.right.data:
        deep_pre(node.right)


def deep_middle(node):
    """middle order scan two branch tree"""
    if node.left.data:
        deep_middle(node.left)
    print(node.data)
    if node.right.data:
        deep_middle(node.right)


def deep_post(node):
    """post order scan two branch tree"""
    if node.left.data:
        deep_post(node.left)
    if node.right.data:
        deep_post(node.right)
    print(node.data)


def deep_pre_store(node, node_list):
    node_list.append(node.data)
    if node.left.data:
        deep_pre_store(node.left, node_list)
    if node.right.data:
        deep_pre_store(node.right, node_list)


def deep_middle_store(node, node_list):
    if node.left.data:
        deep_middle_store(node.left, node_list)
    node_list.append(node.data)
    if node.right.data:
        deep_middle_store(node.right, node_list)


def deep_post_store(node, node_list):
    if node_list.left.data:
        deep_post_store(node.left, node_list)
    if node_list.right.data:
        deep_post_store(node.right, node_list)
    node_list.append(node)


def left_sight(node, node_list, level):
    """use root -> left -> right order"""
    if len(node_list) < level:
        node_list.append(node.data)
    if node.left.data:
        left_sight(node.left, node_list, level + 1)
    if node.right.data:
        left_sight(node.right, node_list, level + 1)


def right_sight(node, node_list, level):
    """use root -> right -> left order"""
    if len(node_list) < level:
        node_list.append(node.data)
    if node.right.data:
        right_sight(node.right, node_list, level + 1)
    if node.left.data:
        right_sight(node.left, node_list, level + 1)


def level_scan(root):
    """broadcast scan branch tree"""
    level = list()
    level.append(root)
    while level:
        node = level.pop(0)
        print(node.data)
        if node.left.data:
            level.append(node.left)
        if node.right.data:
            level.append(node.right)


def level_store(root, node_list):
    level = list()
    level.append(root)
    while level:
        node = level.pop(0)
        node_list.append(node.data)
        if node.left.data:
            level.append(node.left)
        if node.right.data:
            level.append(node.right)


class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Test(object):
    
    def __init__(self, tree_str):
        self.tree_str = tree_str
        self.index = -1

    def create_tree(self, point):
        self.index = self.index + 1
        if self.index >= len(self.tree_str):
            return
        char = self.tree_str[self.index]
        if char != "#":
            point.data = char
            point.left = Node(None)
            point.right = Node(None)
            self.create_tree(point.left)
            self.create_tree(point.right)

    def test(self):
        # no tree
        if not self.tree_str or self.tree_str[0] == "#":
            print([])
        else:
            # create root
            root = Node(self.tree_str[0])
            root.left = Node(None)
            root.right = Node(None)
            # create sons
            if len(self.tree_str) >= 2:
                self.tree_str = self.tree_str[1:]
                self.create_tree(root.left)
                self.create_tree(root.right)
            # print(left sight)
            left_sight_result = list()
            left_sight(root, left_sight_result, 1)
            print(left_sight_result)
            level_scan(root)


if __name__ == "__main__":
    Test("abc##de#g##f###").test()


#  https://www.cnblogs.com/guweiwei/p/7080971.html
#
