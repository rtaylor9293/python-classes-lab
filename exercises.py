class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    
    def print_board(self):
        board = self.board
        print(f"""
                A   B   C
            1)  {board['a1'] or ' '} | {board['b1'] or ' '} | {board['c1'] or ' '}
                ----------
            2)  {board['a2'] or ' '} | {board['b2'] or ' '} | {board['c2'] or ' '}
                ----------
            3)  {board['a3'] or ' '} | {board['b3'] or ' '} | {board['c3'] or ' '}
        """)
    
    def print_message(self):
        if self.tie:
            print('Tie Game!')
        elif self.winner:
            print(f'{self.winner} wins the game!')
        else: 
            print(f'It\'s player {self.turn}\'s turn!')

    def render(self):
        Game.print_board(self)
        Game.print_message(self)
    
    def place_piece(self):
        while True:
            move = input(f'Enter a valid move (example: A1): ').lower()
            if move[0] in ('a', 'b', 'c') and move[1] in ('1', '2', '3') and self.board[move] is None:
                print('Cowabunga!')
                self.board[move] = self.turn
                self.switch_turns()
                break
            else: 
                print('Oh no!  Invalid move.  Try again.')
                self.print_message()

    def switch_turns(self):
        if self.winner:
            return
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn =='O':
            self.turn = 'X'

    def check_for_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']) or self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']) or self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']) or self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']) or self.board['a3'] and (self.board['a3'] == self.board['b2'] == self.board['c1']) or self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']) or self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']) or self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
            self.winner = self.turn
    
    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True

    def play_game(self):
        print('I love me some tic-tac-toe!')
        while not self.winner and not self.tie:
            self.render()
            self.place_piece()
            self.check_for_winner()
            self.check_for_tie()
            if self.winner or self.tie:
                self.render()

tic_tac_toe = Game()
tic_tac_toe.play_game()
