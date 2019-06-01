import random

class MSgame:
    def __init__(self):
        self.difficulty = int(raw_input("Enter 1 for easy, 2 for medium, 3 for hard difficulty..."))
        self.side_len = int(raw_input("Enter an integer for length of the  side..."))
        self.matrix = [[1 if self.difficulty*random.random() > 0.7 else 0 for x in range(0,self.side_len)] for i in range(0,self.side_len)]
        self.show_matrix = [['X' for j in row] for row in self.matrix]
        self.to_check = []
        game_over = False

    def print_matrix(self):

        for row in self.show_matrix:
            for val in row:
                print '{:2}'.format(val),
            print
        
        for row in self.matrix:
            for val in row:
                print '{:2}'.format(val),
            print

    def is_bottom_row(self, i):
        return i > self.side_len**2 - self.side_len

    def is_top_row(self,i):
        return i < self.side_len**2

    def is_left_edge(self,i):
        return i % self.side_len == 0

    def is_right_edge(self, i):
        return i % self.side_len == self.side_len-1

    def check_tile(self, row, col):
        #check for game over
        bomb_count = 0
        #check 8 adjacent tiles, uncover if not bomb:
        #ul
        if not self.is_top_row(row) and not  self.is_left_edge(col):
            if self.matrix[row+1][col-1] == 1:
                bomb_count += 1 
            else:
                 self.to_check.append([row+1,col-1])

        #u
        if not  self.is_top_row(row): 
            if self.matrix[row+1][col] == 1:
                bomb_count += 1 
            else:
                 self.to_check.append([row+1,col])
        #ur
        if not  self.is_top_row(row) and not  self.is_right_edge(col):
            if self.matrix[row+1][col+1] == 1:
                bomb_count += 1 
            else:
                 self.to_check.append([row+1,col+1])
        #l
        if not  self.is_left_edge(col):
            if self.matrix[row][col-1] == 1:
                bomb_count += 1 
            else:
                 self.to_check.append([row,col-1])
        #r
        if not  self.is_right_edge(col):
            if self.matrix[row][col+1] == 1:
                bomb_count += 1 
            else:
                 self.to_check.append([row,col+1])
        #bl
        if not  self.is_bottom_row(row) and not  self.is_left_edge(col):
            if self.matrix[row-1][col-1] == 1:
                bomb_count += 1 
            else:
                 self.to_check.append([row-1,col-1])
        #b
        if not  self.is_bottom_row(row):
            if self.matrix[row-1][col] == 1:
                bomb_count += 1 
            else:
                 self.to_check.append([row-1,col])
        #br
        if not  self.is_bottom_row(row) and not  self.is_right_edge(col):
            if self.matrix[row-1][col-1] == 1:
                bomb_count += 1 
            else:
                 self.to_check.append([row-1,col-1])

        self.show_matrix[row][col] = str(bomb_count)
   
    def check_matrix(self,row,col):
        return self.matrix[row][col]

def main():
    game = MSgame()
    game_over = False
    while not game_over:
        r = raw_input("Enter row to play:")
        c = raw_input("Enter column to play:")
        if game.check_matrix(int(r),int(c)) == 1:
            game_over = True
        game.check_tile(int(r),int(c))
        game.print_matrix()

if __name__ == "__main__":
    main()
