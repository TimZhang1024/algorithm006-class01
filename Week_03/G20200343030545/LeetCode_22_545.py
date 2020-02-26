"""
    给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
    例如，给出 n = 3，生成结果为：
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n > 0:
            self.recursive(0, 0, n, "", res)
        return res

    @classmethod
    def recursive(cls, left: int, right: int, n: int, s: str, res: List[str]):
        # terminator
        if left == n and right == n:
            res.append(s)
            return

        # code logic
        if left < n:
            cls.recursive(left + 1, right, n, s + "(", res)
        if left > right:
            cls.recursive(left, right + 1, n, s + ")", res)
