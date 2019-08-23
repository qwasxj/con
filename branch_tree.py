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

    def create_tree(self, node):
        """abc##de#g##f###"""
        self.index = self.index + 1
        if self.index >= len(self.tree_str):
            return
        char = self.tree_str[self.index]
        if char != "#":
            node.data = char
            node.left = Node(None)
            node.right = Node(None)
            self.create_tree(node.left)
            self.create_tree(node.right)

    @staticmethod
    def build_pre(node, pre_list, middle_list):
        """pre, middle scan list to build tree"""
        if not pre_list:
            return
        char = pre_list[0]
        node.data = char
        char_index = middle_list.index(char)
        middle_left_list = middle_list[:char_index]
        if len(pre_list) > 1 and 1 < char_index:
            pre_left_list = pre_list[1: char_index]
            node.left = Node(None)
            Test.build_pre(node.left, pre_left_list, middle_left_list)
        if char_index + 1 < len(middle_list):
            middle_right_list = middle_list[char_index + 1:]
            pre_right_list = pre_list[char_index + 1:]
            node.right = Node(None)
            Test.build_pre(node.right, pre_right_list, middle_right_list)

    @staticmethod
    def build_post(node, post_list, middle_list):
        """post, middle scan list to build tree"""
        # abc bac bca
        if not post_list:
            return
        char = post_list[-1]
        node.data = char
        char_index = middle_list.index(char)
        middle_left_list = middle_list[:char_index]
        left_index = len(middle_left_list) + 1
        if len(post_list) > left_index:
            post_left_list = post_list[:-left_index]
            node.left = Node(None)
            Test.build_post(node.left, post_left_list, middle_left_list)
        if char_index + 1 < len(middle_list) and len(post_list) > left_index:
            middle_right_list = middle_list[char_index + 1:]
            post_right_list = post_list[-left_index: -2]
            node.right = Node(None)
            Test.build_post(node.right, post_right_list, middle_right_list)

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


# https://www.cnblogs.com/guweiwei/p/7080971.html
# https://baijiahao.baidu.com/s?id=1609200503642486098&wfr=spider&for=pc
