from lcutils.ListNode import build_singlylist


if __name__ == '__main__':
    test_data = ['LEETCODE', [1,2,3,4,5], [3], []]
    for i in test_data:
        n = build_singlylist(i)
        print(n)
        print(n.reverse(n), '\n')
