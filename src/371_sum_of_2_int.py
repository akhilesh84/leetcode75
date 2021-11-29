class Solution:
    def getSum(self, a: int, b: int) -> int:
        return 0

if __name__ == '__main__':
    test_data = [(1,2), (2764, 98536), (-1, -9468)]
    s = Solution()
    for (a,b) in test_data:
        print("{} + {} = {}".format( a, b, s.getSum(a, b)))

