class Block:
    def __init__(self, data:list):
        self.block = data

    def get_data_pos(self, num):
        return self.block[num]

    def row1(self):
        return self.block[:3]

    def row2(self):
        return self.block[3:6]

    def row3(self):
        return self.block[6:]


class Board:
    def __init__(self):
        self.BL1 = Block([0, 0, 4, 0, 0, 2, 5, 1, 0])
        self.BL2 = Block([0, 0, 8, 0, 0, 5, 0, 7, 0])
        self.BL3 = Block([0, 5, 7, 0, 0, 3, 0, 8, 4])
        self.BL4 = Block([0, 2, 6, 0, 5, 8, 0, 0, 0])
        self.BL5 = Block([0, 1, 0, 3, 6, 0, 8, 2, 9])
        self.BL6 = Block([3, 7, 0, 0, 0, 0, 0, 6, 0])
        self.BL7 = Block([4, 0, 0, 2, 0, 0, 0, 0, 0])
        self.BL8 = Block([7, 0, 0, 6, 9, 0, 4, 8, 0])
        self.BL9 = Block([8, 3, 2, 7, 0, 5, 0, 9, 0])

        self.board = [
            [self.BL1, self.BL2, self.BL3],
            [self.BL4, self.BL5, self.BL6],
            [self.BL7, self.BL8, self.BL9]
        ]

    def __str__(self):
        space = " "
        row1 = f'  {self.BL1.row1()}  {self.BL2.row1()}  {self.BL3.row1()}'
        row2 = f'  {self.BL1.row2()}  {self.BL2.row2()}  {self.BL3.row2()}'
        row3 = f'  {self.BL1.row3()}  {self.BL2.row3()}  {self.BL3.row3()}'
        
        row4 = f'  {self.BL4.row1()}  {self.BL5.row1()}  {self.BL6.row1()}'
        row5 = f'  {self.BL4.row2()}  {self.BL5.row2()}  {self.BL6.row2()}'
        row6 = f'  {self.BL4.row3()}  {self.BL5.row3()}  {self.BL6.row3()}'

        row7 = f'  {self.BL7.row1()}  {self.BL8.row1()}  {self.BL9.row1()}'
        row8 = f'  {self.BL7.row2()}  {self.BL8.row2()}  {self.BL9.row2()}'
        row9 = f'  {self.BL7.row3()}  {self.BL8.row3()}  {self.BL9.row3()}'
        
        return f'\n\n{row1}\n{row2}\n{row3}\n{space}\n{row4}\n{row5}\n{row6}\n{space}\n{row7}\n{row8}\n{row9}\n\n'


b = Board()
print(b.BL1.get_data_pos(3))