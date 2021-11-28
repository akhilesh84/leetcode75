from lcutils.ListNode import build_singlylist

if __name__ == '__main__':
    test_data = [('LEETCODE', 8), ([1,2,3,4,5], 5), ([3],1), ([1],1)]
    for (data, index) in test_data:
        n = build_singlylist(data)
        print(n)
        print(n.removeNthFromEnd(n, index), '\n')
