import random

class MSgame:
    def __init__(self):
        self.difficulty = int(raw_input("Enter 1 for easy, 2 for medium, 3 for hard difficulty..."))
        self.side_len = int(raw_input("Enter an integer for length of the  side..."))
        self.matrix = [[9 if self.difficulty*random.random() > 0.9 else 0 for x in range(0,self.side_len)] for i in range(0,self.side_len)]
        for i in range(0,self.side_len):
            for j in range(0,self.side_len):
                    self.bomb_counter(i,j)
        self.show_matrix = [['X' for j in row] for row in self.matrix]

    def print_matrix(self):
        for row in self.show_matrix:
            for val in row:
                print '{:2} '.format(val),
            print

    def is_bottom_row(self, i):
        return i == self.side_len - 1

    def is_top_row(self,i):
        return i == 0

    def is_left_edge(self,i):
        return i == 0

    def is_right_edge(self, i):
        return i == self.side_len-1

    def bomb_counter(self, row, col):
        if self.matrix[row][col] == 9:
            return
        bomb_count = 0
        if not self.is_top_row(row) and not  self.is_left_edge(col):
            if self.matrix[row-1][col-1] == 9:
                bomb_count += 1
        if not  self.is_top_row(row):
            if self.matrix[row-1][col] == 9:
                bomb_count += 1
        if not  self.is_top_row(row) and not  self.is_right_edge(col):
            if self.matrix[row-1][col+1] == 9:
                bomb_count += 1
        if not  self.is_left_edge(col):
            if self.matrix[row][col-1] == 9:
                bomb_count += 1
        if not  self.is_right_edge(col):
            if self.matrix[row][col+1] == 9:
                bomb_count += 1
        if not  self.is_bottom_row(row) and not  self.is_left_edge(col):
            if self.matrix[row+1][col-1] == 9:
                bomb_count += 1
        if not  self.is_bottom_row(row):
            if self.matrix[row+1][col] == 9:
                bomb_count += 1
        if not  self.is_bottom_row(row) and not  self.is_right_edge(col):
            if self.matrix[row+1][col+1] == 9:
                bomb_count += 1
        self.matrix[row][col] = bomb_count

    def check_matrix(self,row,col):
        for i in self.show_matrix:
            for j in i:
                if j == 'X':
                    return self.matrix[row][col]
        return 10;

    def play_move(self, row, col):
        self.show_matrix[row][col] = str(self.matrix[row][col])
        if not self.is_top_row(row) and not  self.is_left_edge(col):
            self.show_matrix[row-1][col-1] = str(self.matrix[row-1][col-1])
        if not  self.is_top_row(row):
            self.show_matrix[row-1][col] = str(self.matrix[row-1][col])
        if not  self.is_top_row(row) and not  self.is_right_edge(col):
            self.show_matrix[row-1][col+1] = str(self.matrix[row-1][col+1])
        if not  self.is_left_edge(col):
            self.show_matrix[row][col-1] = str(self.matrix[row][col-1])
        if not  self.is_right_edge(col):
            self.show_matrix[row][col+1] = str(self.matrix[row][col+1])
        if not  self.is_bottom_row(row) and not  self.is_left_edge(col):
            self.show_matrix[row+1][col-1] = str(self.matrix[row+1][col-1])
        if not  self.is_bottom_row(row):
            self.show_matrix[row+1][col] = str(self.matrix[row+1][col])
        if not  self.is_bottom_row(row) and not  self.is_right_edge(col):
            self.show_matrix[row+1][col+1] = str(self.matrix[row+1][col+1])

def main():
    game = MSgame()
    game_over = False
    while not game_over:
        game.print_matrix()
        r = raw_input("Enter row to play:")
        c = raw_input("Enter column to play:")
        if game.check_matrix(int(r),int(c)) == 9:
            print "You lost"
            game_over = True
        elif game.check_matrix(int(r),int(c)) == 10:
            print "You won!"
            game_over = True
        game.play_move(int(r),int(c))

if __name__ == "__main__":
    main()
