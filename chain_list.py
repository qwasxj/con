

class SingleChainList(object):

    def __init__(self, data="", post=None):
        self.data = data
        self.post = post


class TestSingleChain(object):

    def __init__(self, data_list):
        self.data_list = data_list

    @staticmethod
    def build_chain_sec(root, data_list):
        if not data_list:
            return
        root.post = SingleChainList()
        root.post.data = data_list[0]
        if len(data_list) > 1:
            TestSingleChain.build_chain_sec(root.post, data_list[1:])

    @staticmethod
    def build_chain(root, data_list):
        node = root
        for data in data_list:
            node.post = SingleChainList(data)
            node = node.post
        return root

    @staticmethod
    def find_first(root, data):
        point = root
        while point.post:
            point = point.post
            if point.data == data:
                return True, point
        return False, root

    @staticmethod
    def insert(root, data, index):
        i = -1
        while root:
            i = i + 1
            if i == index:
                node = SingleChainList(data)
                node.post = root.post
                root.post = node
                return
            root = root.post
        raise Exception("index out of range")

    @staticmethod
    def delete(root, index):
        i = -1
        while root:
            i = i + 1
            if i == index and root.post:
                root.post = root.post.post
                return
            if i == index and not root.post:
                root.post = None
            root = root.post
        raise Exception("index output of range")

    @staticmethod
    def scan(root):
        while root.post:
            root = root.post
            print(root.data)

    @staticmethod
    def reverse(root):
        point = root
        temp_root = SingleChainList()
        while point.post:
            point = point.post
            node = SingleChainList(point.data)
            node.post = temp_root.post
            temp_root.post = node
        root.post = temp_root.post

    def test(self):
        root = SingleChainList()
        self.build_chain(root, self.data_list)
        # self.scan(root)
        # self.reverse(root)
        self.insert(root, "xx", 4)
        self.scan(root)
        self.delete(root, 1)
        self.scan(root)


class DoubleChainList(object):

    def __init__(self, data="", pre=None, post=None):
        self.data = data
        self.pre = pre
        self.post = post


class TestDoubleChain(object):

    def __init__(self, data_list):
        self.data_list = data_list

    @staticmethod
    def build_chain(root, data_list):
        point = root
        if not data_list:
            return
        for data in data_list:
            node = DoubleChainList(data)
            node.post = point.post
            node.pre = point
            point.post = node
            point = point.post

    @staticmethod
    def build_chain_sec(root, data_list):
        if not data_list:
            return
        node = DoubleChainList(data_list[0])
        node.post = root.post
        node.pre = root
        root.post = node
        if len(data_list) > 1:
            TestDoubleChain.build_chain_sec(node, data_list[1:])

    @staticmethod
    def insert(root, data, index):
        i = -1
        while root:
            i = i + 1
            if i == index:
                node = DoubleChainList(data)
                node.post = root.post
                node.pre = root
                root.post = node
                if node.post:
                    node.post.pre = node
                return
            root = root.post
        raise Exception("index out of range")

    @staticmethod
    def delete(root, index):
        i = -1
        while root:
            i = i + 1
            if i == index and root.post:
                root.post = root.post.post
                if root.post:
                    root.post.pre = root
                return
            if i == index and not root.post:
                root.post = None
            root = root.post
        raise Exception("index out of range")

    @staticmethod
    def reverse(root):
        point = root
        temp_root = DoubleChainList()
        while point.post:
            node = DoubleChainList(point.post.data)
            node.post = temp_root.post
            node.pre = temp_root
            temp_root.post = node
            if node.post:
                node.post.pre = node
            point = point.post
        root.post = temp_root.post

    @staticmethod
    def scan(root):
        while root.post:
            print(root.post.data)
            root = root.post

    def test(self):
        root = DoubleChainList()
        self.build_chain_sec(root, self.data_list)
        # self.scan(root)
        # self.reverse(root)
        # self.scan(root)
        self.insert(root, "xx", 4)
        self.scan(root)
        self.delete(root, 4)
        self.scan(root)


if __name__ == "__main__":
    # t_c = TestSingleChain(["a", "b", "c", "d"])
    # t_c.test()
    t_c = TestDoubleChain([1, 2, 3, 4])
    t_c.test()
