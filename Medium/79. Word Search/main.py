from typing import List, Tuple
class Solution:
    shape = (0 , 0)
    
    def exist(self, board:List[List[str]], word:str) -> bool:
        self.shape = len(board) - 1, len(board[0]) - 1
        # print(f'Rows: {self.shape[0]}, Colums: {self.shape[1]}')
        for row_index, row in enumerate(board):
            for column_index, cell in enumerate(row):
                if cell == word[0]:
                    if self.get_neighbors(board = board, matrix_index=(row_index, column_index), used_matrix_indexes = [(row_index, column_index)], remaining_word = word[1:]):
                        return True
        return False

    def get_neighbors(self, board: List[List[str]], matrix_index:Tuple[int, int], used_matrix_indexes:List[Tuple[int, int]],remaining_word:str):
        if not remaining_word:
            return True
        row, column = matrix_index
        possible_neighbors = []
        if row > 0 :
            possible_neighbors.append((row - 1, column))
        if row < self.shape[0]:
            possible_neighbors.append((row + 1, column))
        if column > 0:
            possible_neighbors.append((row, column - 1))
        if column < self.shape[1]:
            possible_neighbors.append((row, column + 1))


        for row, column in possible_neighbors:
            if (row,column) in used_matrix_indexes:
                continue
            if board[row][column] == remaining_word[0]:
                if self.get_neighbors(board=board, matrix_index=(row, column), used_matrix_indexes=used_matrix_indexes + [(row,column)], remaining_word=remaining_word[1:]):
                    return True
        return False
