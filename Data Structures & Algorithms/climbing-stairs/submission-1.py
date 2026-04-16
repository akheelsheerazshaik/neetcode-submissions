class Solution:
    def climbStairs(self, n: int) -> int:
        current = 1
        previous = 1

        for _ in range(n - 1):
            temp = current
            current = current + previous
            previous = temp

        return current