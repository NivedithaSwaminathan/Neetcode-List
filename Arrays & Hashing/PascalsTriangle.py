# We will use a list of lists to create the triangle, with each row being denoted by a list.
# We iterate through the number of rows. For each row, the first and last element will be 1.
# We compute the middle elements as the sum of elements from the previous row, same column and previous row, previous column.
# Each row list is appended to the result list.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        tri = []
        tri.append([1])

        for row in range(1,numRows):

            curr = [1]* (row+1)

            for col in range(len(curr)):

                if col != 0 and col != len(curr)-1:

                    curr[col] = tri[row-1][col] + tri[row-1][col-1]

            tri.append(curr)

        return tri
