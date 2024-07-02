import random
import regex as re
# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object" 
# or "dig here" or "render this board for this object"
class Board:
    

    def __init__(self, dim_size, num_bombs):
        
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function!
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered 
        # we'll save (row,col) tuples into this set
        self.dug = set()

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists (or whatever representation you prefer
        # but since we have a 2D board, list of lists is natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates a board something like this
        # [ [None, None, ..., None],
        #   [None, None, ..., None],
        #   [       .              
        #           .
        #           .             ]
        #   [None, None, ..., None] ]
        # we can see this represents a board

        # plant the bombs
        bombs_planted =  0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0,self.dim_size**2 -1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size
            col = loc % self. dim_size

            if board[row][col] == "*":
                continue
                # this means we've actually planted a bomb there already so keep going
            board[row][col] = '*'
            bombs_planted += 1

        return board
                
    def assign_values_to_board(self):

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    # if there is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] =  self.get_num_neighbouring_bombs(r,c)
    
    def get_num_neighbouring_bombs(self,row,col):
        # Let's iterate through each of the neighbouring positions and sum the number of bombs

        num_neighbouring_bombs = 0
        for r in range(max(0,row-1), min((row+1),self.dim_size-1) + 1):
            for c in range(max(0,col-1), min((col+1), self.dim_size-1) + 1):
                if r == row and c == col:
                    continue
                else:
                    num_neighbouring_bombs += 1
        return num_neighbouring_bombs

    def dig(self, row, col):
        # dig at a location !
        # return True is successful dig, False if dug bomb

        self.dug.add((row,col)) # to keep track

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col]:
            return True

        # self.board[row][col] == 0 
        for r in range(max(0,row-1), min((row+1),self.dim_size-1) + 1):
            for c in range(max(0,col-1), min((col+1), self.dim_size-1) + 1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
            
        return True 

    def __str__(self):

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size,num_bombs)
    # Step 3: show the user the board and ask for where they want to dig
    # Step 3a: if location is bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repeat Steps 2 and 3a/b until there are no more places to dig - VICTORY!

    safe = True

    while len(board.dug) < board.dim_size**2:
        print(board)
        user_input = re.split(',(\\s)*',input("Where to dig next?(Eg: 1, 2)"))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col>= board.dim_size:
            print("Invalid Location. Try again")
            continue
        
        safe = board.dig(row,col)
        if not safe:
            break
    
    if safe:
        print("Congratulations!!!")
    else:
        print("Sorry. Game Over")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

    

if __name__ == '__main__':
    play()