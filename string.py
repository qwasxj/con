#! /usr/bin/python
# -*- coding: utf-8 -*-


class String(object):

    @staticmethod
    def full_queue(s):
        """字符串全排列"""
        if len(s) <= 1:
            return [s]
        str_list = list()
        for i in range(len(s)):
            for son_queue in String.full_queue(s[:i] + s[i + 1:]):
                str_list.append(s[i] + son_queue)
        return str_list

    @staticmethod
    def all_sub_string(s):
        sub_list = list()
        for i in range(len(s)):
            for index in range(len(s) - i):
                sub_list.append(s[index: index + (i + 1)])
        return sub_list

    @staticmethod
    def all_common_string(s1, s2):
        """所有公共子串"""
        return list(
            set(String.all_sub_string(s1)) & set(String.all_sub_string(s2))
        )

    @staticmethod
    def max_common_string(s1, s2):
        """最大公共子串"""
        commons = String.all_common_string(s1, s2)
        if not commons:
            raise Exception("no common string")
        max_str = commons[0]
        for common in commons:
            if len(common) > len(max_str):
                max_str = common
        return max_str

    @staticmethod
    def test():
        # print(self.full_queue("123"))
        s1 = "123"
        s2 = "234"
        common = String.all_common_string(s1, s2)
        print(common)
        print(String.max_common_string(s1, s2))


if __name__ == "__main__":
    String().test()
