# Programming Exercise 15
# 15 Find a sudoku puzzle. Write a program to solve it. 

class Block:
    def __init__(self, data):
        self.block = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def getPos(self, num):
        return self.block[num]


class Board:
    def __init__(self):
        self.BL1 = Block(block_1)
        self.BL2 = Block(block_2)
        self.BL3 = Block(block_3)
        self.BL4 = Block(block_4)
        self.BL5 = Block(block_5)
        self.BL6 = Block(block_6)
        self.BL7 = Block(block_7)
        self.BL8 = Block(block_8)
        self.BL9 = Block(block_9)

        self.board = [
            [self.BL1, self.BL2, self.BL3],
            [self.BL4, self.BL5, self.BL6],
            [self.BL7, self.BL8, self.BL9]
        ]

    def __str__(self):
        space = " "
        row1 = f'  {self.BL1.getPos(0)}  {self.BL2.getPos(0)}  {self.BL3.getPos(0)}'
        row2 = f'  {self.BL1.getPos(1)}  {self.BL2.getPos(1)}  {self.BL3.getPos(1)}'
        row3 = f'  {self.BL1.getPos(2)}  {self.BL2.getPos(2)}  {self.BL3.getPos(2)}'
        
        row4 = f'  {self.BL4.getPos(0)}  {self.BL5.getPos(0)}  {self.BL6.getPos(0)}'
        row5 = f'  {self.BL4.getPos(1)}  {self.BL5.getPos(1)}  {self.BL6.getPos(1)}'
        row6=  f'  {self.BL4.getPos(2)}  {self.BL5.getPos(2)}  {self.BL6.getPos(2)}'

        row7 = f'  {self.BL7.getPos(0)}  {self.BL8.getPos(0)}  {self.BL9.getPos(0)}'
        row8 = f'  {self.BL7.getPos(1)}  {self.BL8.getPos(1)}  {self.BL9.getPos(1)}'
        row9 = f'  {self.BL7.getPos(2)}  {self.BL8.getPos(2)}  {self.BL9.getPos(2)}'
        
        return f'{row1}\n{row2}\n{row3}\n{space}\n{row4}\n{row5}\n{row6}\n{space}\n{row7}\n{row8}\n{row9}'

       


b = Board()
print(b)