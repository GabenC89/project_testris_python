import pygame
from engine.gameObject import GameObject

class GameBoard(GameObject):
    def __init__(self, pos_x, pos_y, width_in_blocks, height_in_blocks, block_size=50, image_path = None, fill_color = (0,0,0)):
        super().__init__(pos_x, pos_y, (width_in_blocks * block_size), (height_in_blocks * block_size), image_path, fill_color)

        self.grid = []
        for i in range(height_in_blocks):
            row = []
            for j in range(width_in_blocks):
                row.append('X')
            self.grid.append(row)

        self.row_number = height_in_blocks
        self.col_number = width_in_blocks

    def __str__(self):
        print("Debug grid is the following")
        str = f''
        for i in range(self.row_number):
            for j in range(self.col_number):
                str += f'{self.grid[i][j]} ' 
            str += '\n'
        return str