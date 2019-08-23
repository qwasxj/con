

class SortStack(object):

    def __init__(self):
        """stack top left, stack button right"""
        self.data_list = list()

    def push(self, value):
        self.data_list.insert(0, value)

    def pop(self):
        if not self.data_list:
            raise Exception("pop index out of range")
        return self.data_list.pop(0)

    def is_stack_empty(self):
        return self.data_list == []


class TestSortStack(object):

    @staticmethod
    def stack_iter(s):
        while not s.is_stack_empty():
            yield s.pop()

    def test(self):
        arr = [1, 2, 3, 4, 5, 6]
        s = SortStack()
        for ele in arr:
            s.push(ele)
        for e in self.stack_iter(s):
            print(e)


class SingleChainList(object):

    def __init__(self, data="", post=None):
        self.data = data
        self.post = post


class ListStack(object):

    def __init__(self):
        self.root = SingleChainList()

    def push(self, data):
        node = SingleChainList(data)
        node.post = self.root.post
        self.root.post = node

    def pop(self):
        if not self.root.post:
            raise Exception("pop index out of range")
        data = self.root.post.data
        self.root.post = self.root.post.post
        return data

    def is_stack_empty(self):
        return self.root.post is None


class TestListStack(object):

    @staticmethod
    def stack_iter(stack):
        while not stack.is_stack_empty():
            yield stack.pop()

    def test(self):
        arr = [1, 2, 3, 4, 5, 6]
        s = ListStack()
        for ele in arr:
            s.push(ele)
        for ele in self.stack_iter(s):
            print(ele)


class SortQueue(object):

    def __init__(self):
        """left is tail and right is head"""
        self.data_list = list()

    def en_queue(self, value):
        self.data_list.insert(0, value)

    def de_queue(self):
        if not self.data_list:
            raise Exception("de_queue index out of range")
        return self.data_list.pop(-1)

    def is_queue_empty(self):
        return self.data_list == []


class TestSortQueue(object):

    @staticmethod
    def queue_iter(queue):
        while not queue.is_queue_empty():
            yield queue.de_queue()

    def test(self):
        arr = [1, 2, 3, 4]
        q = SortQueue()
        for ele in arr:
            q.en_queue(ele)
        for ele in self.queue_iter(q):
            print(ele)


class ListQueue(object):

    def __init__(self):
        """tail is enter and head is de"""
        self.root = SingleChainList()

    def en_queue(self, data):
        point = self.root
        while point.post:
            point = point.post
        node = SingleChainList(data)
        point.post = node

    def de_queue(self):
        if not self.root.post:
            raise Exception("de_queue index out of range")
        data = self.root.post.data
        self.root.post = self.root.post.post
        return data

    def is_queue_empty(self):
        return self.root.post is None


class TestListQueue(object):

    @staticmethod
    def queue_iter(queue):
        while not queue.is_queue_empty():
            yield queue.de_queue()

    def test(self):
        arr = [1, 2, 3, 4]
        q = ListQueue()
        for ele in arr:
            q.en_queue(ele)
        for ele in self.queue_iter(q):
            print(ele)


if __name__ == "__main__":
    # TestSortStack().test()
    # TestListStack().test()
    # TestSortQueue().test()
    TestListQueue().test()
