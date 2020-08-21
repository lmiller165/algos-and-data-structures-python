# Programming Exercise 15
# 15 Find a sudoku puzzle. Write a program to solve it. 

class Block:
    def __init__(self):
        self.block = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
    def __repr__(self):
        new_row = '+ - + - + - + '
        final_row = '--------------'
        row1 = f'  {self.block[0][0]}   {self.block[0][1]}   {self.block[0][2]} |' 
        row2 = f'  {self.block[1][0]}   {self.block[1][1]}   {self.block[1][2]} |' 
        row3 = f'  {self.block[2][0]}   {self.block[2][1]}   {self.block[2][2]} |' 
        return f"{new_row}\n{row1}\n{new_row}\n{row2}\n{new_row}\n{row3}\n{final_row}"

    def __str__(self):
        new_row = '+ - + - + - + '
        final_row = '--------------'
        row1 = f'  {self.block[0][0]}   {self.block[0][1]}   {self.block[0][2]} |' 
        row2 = f'  {self.block[1][0]}   {self.block[1][1]}   {self.block[1][2]} |' 
        row3 = f'  {self.block[2][0]}   {self.block[2][1]}   {self.block[2][2]} |' 
        return f"{new_row}\n{row1}\n{new_row}\n{row2}\n{new_row}\n{row3}\n{final_row}"

    def getPos(self, num):
        return self.block[num]


class Board:
    def __init__(self):
        self.BL1 = Block()
        self.BL2 = Block()
        self.BL3 = Block()
        self.BL4 = Block()
        self.BL5 = Block()
        self.BL6 = Block()
        self.BL7 = Block()
        self.BL8 = Block()
        self.BL9 = Block()

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