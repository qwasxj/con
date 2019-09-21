
class Heap(object):

    """large root heap"""

    @staticmethod
    def build(seq):
        temp = list(seq)
        while seq:
            seq.pop(0)
        for ele in temp:
            Heap.insert(seq, ele)

    @staticmethod
    def shift_up(seq, index):
        father = (index - 1) / 2
        if father >= 0 and seq[father] < seq[index]:
            temp = seq[index]
            seq[index] = seq[father]
            seq[father] = temp
            Heap.shift_up(seq, father)

    @staticmethod
    def shift_down(seq, index):
        m_index = 2 * index + 1
        # no son node
        if m_index >= len(seq):
            return
        # just left son node
        if (m_index < len(seq)) and (m_index + 1 >= len(seq)):
            # father node shift down
            if seq[index] < seq[m_index]:
                temp = seq[index]
                seq[index] = seq[m_index]
                seq[m_index] = temp
            return
        # two son node, find larger son node
        if seq[m_index] < seq[m_index + 1]:
            m_index = m_index + 1
        if seq[index] < seq[m_index]:
            temp = seq[index]
            seq[index] = seq[m_index]
            seq[m_index] = temp
            Heap.shift_down(seq, m_index)

    @staticmethod
    def heap_sort(seq):
        Heap.build(seq)
        heap = list(seq)
        while seq:
            seq.pop(0)
        while heap:
            print(heap)
            seq.insert(0, Heap.remove(heap, 0))

    @staticmethod
    def insert(seq, ele):
        seq.append(ele)
        Heap.shift_up(seq, len(seq) - 1)

    @staticmethod
    def remove(seq, index):
        if index < 0 or index >= len(seq):
            raise Exception("index out of range")
        remove_node = seq.pop(index)
        if seq:
            seq.insert(index, seq.pop(-1))
            if index != 0 and seq[index] > seq[(index - 1) / 2]:
                Heap.shift_up(seq, index)
            else:
                Heap.shift_down(seq, index)
        return remove_node

    @staticmethod
    def replace(seq, index, ele):
        if index < 0 or index >= len(seq):
            raise Exception("index out of range")
        seq[index] = ele
        if seq[index] > seq[(index - 1) / 2]:
            Heap.shift_up(seq, index)
        else:
            Heap.shift_down(seq, index)


class Sort(object):

    @staticmethod
    def insert_sort(seq):  # O(n^2)
        for i in range(1, len(seq)):
            num = seq[i]
            index = i
            while index:
                if num < seq[index - 1]:
                    seq[index] = seq[index - 1]
                else:
                    break
                index -= 1
            seq[index] = num

    @staticmethod
    def hell_sort(seq):
        pass

    @staticmethod
    def select_sort(seq):  # O(n^2)
        for i in range(len(seq)):
            min_index = i
            for j in range(i, len(seq), 1):
                if seq[j] < seq[min_index]:
                    min_index = j
            temp = seq[i]
            seq[i] = seq[min_index]
            seq[min_index] = temp

    @staticmethod
    def heap_sort(seq):
        Heap.heap_sort(seq)

    @staticmethod
    def bubble_sort(seq):  # O(n^2)
        sort_len = len(seq) - 1
        while sort_len >= 0:
            for i in range(0, sort_len, 1):
                if seq[i] > seq[i + 1]:
                    temp = seq[i + 1]
                    seq[i + 1] = seq[i]
                    seq[i] = temp
            sort_len -= 1

    @staticmethod
    def quick_sort(seq):  # O(nlogn)
        if not len(seq):
            return []
        # find base right position
        temp = seq[0]
        pre = 0
        post = len(seq) - 1
        after = True
        while pre != post:
            if after and seq[post] < temp:
                seq[pre] = seq[post]
                after = False
                pre += 1
            elif after and seq[post] >= temp:
                post -= 1
            elif not after and seq[pre] > temp:
                seq[post] = seq[pre]
                after = True
                post -= 1
            else:
                pre += 1
        return Sort.quick_sort(seq[: pre]) + \
            [temp] + Sort.quick_sort(seq[pre + 1:])

    @staticmethod
    def merge(left_seq, right_seq):
        temp = list()
        while len(left_seq) and len(right_seq):
            if left_seq[0] < right_seq[0]:
                temp.append(left_seq.pop(0))
            else:
                temp.append(right_seq.pop(0))
        while len(left_seq):
            temp.append(left_seq.pop(0))
        while len(right_seq):
            temp.append(right_seq.pop(0))
        return temp

    @staticmethod
    def merge_sort(seq):  # O(nlogn)
        if len(seq) == 1:
            return seq
        middle = len(seq) / 2
        left_seq = Sort.merge_sort(seq[0:middle])
        right_seq = Sort.merge_sort(seq[middle:])
        return Sort.merge(left_seq, right_seq)


if __name__ == "__main__":
    que = [3, 7, 4, 2, 1, 5, 1, 2]
    Sort.heap_sort(que)
    print(que)
