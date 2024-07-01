# This is my first approach using the classes
# It is able to solve any easy level problem
# The problem with this is the solution class is not copyable like array
# Difficult to implement dynamic programming






from time import sleep, time


def displayCurrentPosition(arr: list):

    for i in range(0, 9):
        for j in range(0, 9):
            print(arr[i][j].val if arr[i][j].val else ".", end="  ")
        print()
    print()
    print()
    pass


# arr = [
#     [2, 0, 0, 6, 0, 0, 8, 3, 0],
#     [9, 0, 8, 5, 3, 0, 6, 0, 2],
#     [0, 0, 1, 8, 0, 7, 0, 4, 0],
#     [0, 6, 0, 0, 5, 3, 0, 0, 0],
#     [7, 0, 4, 2, 0, 8, 0, 0, 0],
#     [0, 2, 0, 4, 9, 6, 0, 0, 0],
#     [0, 8, 0, 0, 6, 0, 0, 0, 5],
#     [0, 0, 0, 1, 0, 5, 7, 6, 3],
#     [5, 0, 6, 3, 0, 4, 0, 0, 0],
# ]


class solution:
    def __init__(self, row, col, val) -> None:
        self.row = row
        self.col = col
        self.box = (self.row // 3) * 3 + self.col // 3 + 1
        self.val = val
        if not val:
            self.possibleArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.len = 9

    def pencil(self):
        for i in self.possibleArr:
            if i:
                self.val = i
                # print(self.row,self.col,self.possibleArr)
                # print()
                # displayCurrentPosition(arr)
                continue        
        return 1

    def remove(self, num):
        cnt = 0
        if self.possibleArr[num - 1]:
            self.possibleArr[num - 1] = 0
            self.len -= 1
            if self.len == 1:
                cnt += self.pencil()
                cnt += self.clear()
        return cnt

    # def box_iterator(self, func):
    #     row = self.row // 3
    #     col = self.col // 3
    #     for i in range(row, row + 3):
    #         for j in range(col, col + 3):
    #             if not arr[i][j].val:
    #                 func(arr[i][j])

    def clear(self):
        cnt = 0
        for i in range(9):
            if not arr[self.row][i].val:
                cnt += arr[self.row][i].remove(self.val)
                # print(self.row,self.row,i,self.col,self.val,arr[self.row][i].possibleArr)

        for i in range(9):
            if not arr[i][self.col].val:
                cnt += arr[i][self.col].remove(self.val)
                # print(self.row,i,self.col,self.col,self.val,arr[i][self.col].possibleArr)

        row = self.row - self.row % 3
        col = self.col - self.col % 3
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if not arr[i][j].val:
                    cnt += arr[i][j].remove(self.val)
                    # print(self.row,i,j,self.col,self.val,arr[i][j].possibleArr)
        return cnt


def sudukoSolver(arr):
    cnt = 0
    arr2 = arr.copy()
    for i in range(9):
        for j in range(9):
            if arr[i][j]:
                cnt += 1
            arr[i][j] = solution(i, j, arr[i][j])

    # displayCurrentPosition(arr)

    for i in range(9):
        for j in range(9):
            if arr[i][j].val:
                cnt += arr[i][j].clear()

    # print(cnt)
    # print(arr[0][7].possibleArr)
    # print(arr[6][2].possibleArr)


arr = list()
for i in range(9):
    l2 = list(map(int, input().split()))
    arr.append(l2)


st = time()
sudukoSolver(arr)
end = time()
displayCurrentPosition(arr)

print(end - st)


"""
# Medium
0 4 0 8 0 0 0 0 0
2 1 0 6 5 0 0 0 0
3 0 6 4 0 0 0 2 9
0 5 0 0 0 0 1 0 4
0 0 0 0 0 0 0 0 0
6 0 1 0 0 0 0 5 0
5 6 0 0 0 4 3 0 1
0 0 0 0 7 3 0 4 5
0 0 0 0 0 1 0 8 0


easy
0 0 0 5 0 3 0 0 4
0 0 2 0 0 1 3 0 6
0 0 9 8 0 6 0 5 0
1 9 8 0 0 0 0 0 0
5 0 4 9 0 2 8 0 1
0 0 0 0 0 0 9 4 3
0 8 0 3 0 9 2 0 0
4 0 1 6 0 0 5 0 0
9 0 0 2 0 5 0 0 0


Solution Easy
8  1  6  5  2  3  7  9  4
7  5  2  4  9  1  3  8  6
3  4  9  8  7  6  1  5  2
1  9  8  7  3  4  6  2  5
5  3  4  9  6  2  8  7  1
2  6  7  1  5  8  9  4  3
6  8  5  3  4  9  2  1  7
4  2  1  6  8  7  5  3  9
9  7  3  2  1  5  4  6  8
"""
