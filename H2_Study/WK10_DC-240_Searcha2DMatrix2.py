'''
=========================================================
240. Search a 2D Matrix II
링크: https://leetcode.com/problems/search-a-2d-matrix-ii/
level: medium
=========================================================
'''

# for문 - O(N)
class Solution:
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False   

if __name__ == '__main__':
    matrix = [[1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    solution = Solution()
    print(solution.searchMatrix(matrix,target))

