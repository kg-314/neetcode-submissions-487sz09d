class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix) - 1
        selected_row = -1

        while l_row <= r_row:
            m_row = (l_row + r_row) // 2

            print(m_row)
            row_vals = matrix[m_row]

            if target >= row_vals[0] and target <= row_vals[len(row_vals) - 1]:
                selected_row = row_vals
                break
            elif target < row_vals[0]:
                r_row = m_row - 1
            else:
                l_row = m_row + 1
        
        if selected_row == -1:
            return False

        l = 0
        r = len(selected_row) - 1

        while l <= r:
            m = (l + r) // 2
            val = selected_row[m]

            if target == val:
                return True
            elif target < val:
                r = m - 1
            else:
                l = m + 1
        return False