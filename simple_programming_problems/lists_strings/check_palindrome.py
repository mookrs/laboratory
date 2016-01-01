# coding: utf-8
"""
    写个函数测试一个字符串是否是回文。
"""
# All of these are O(n)


def is_alindrome_1(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])


def is_palindrome_2(s):
    for i in range(len(s)) / 2:
        if not s[i] == s[len(s) - i - 1]:
            return False
    return True


def is_alindrome_3(s):
    return s == s[::-1]
